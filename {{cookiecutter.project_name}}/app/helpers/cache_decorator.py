import hashlib
import json
import logging
from decimal import Decimal
from functools import wraps
from typing import Callable, Optional

from django.conf import settings
from django.core.cache import caches
from helpers.json import CustomJSONEncoder
from rest_framework.request import Request
from rest_framework.response import Response
from sentry_sdk import capture_exception

logger = logging.getLogger("api_cache")


class CacheDecorator:
    """Decorator that can retrieve and save view's response."""

    def __init__(
        self, prefix=str, alias=str, timeout=int,
    ):
        self.prefix = prefix
        self.alias = alias
        self.timeout = timeout

    def __call__(self, func) -> Callable[..., Response]:
        """Handle request call."""

        @wraps(func)
        def cache_wrapper(_self, request: Request, *args, **kwargs) -> Response:
            response = self.cache_get(request, *args, **kwargs)
            if response:
                return response

            response = func(_self, request, *args, **kwargs)
            self.cache_save(response, request, *args, **kwargs)
            return response

        return cache_wrapper

    @property
    def cache(self):
        """Cache property."""
        return caches[self.alias]

    @classmethod
    def cache_build_hash(cls, request, *args, **kwargs) -> str:
        """Build hash from view's args and kwargs parameters."""
        parts = []

        for arg in args:
            parts.append(str(arg))

        kwarg_items = [(str(key), str(value)) for key, value in kwargs.items()]  # noqa: WPS221
        kwarg_items = kwarg_items + [
            (str(key), str(value)) for key, value in request.query_params.items()
        ]  # noqa: WPS221
        kwarg_items.sort()
        for key, value in kwarg_items:
            parts.append("{key}:{value}".format(key=key, value=value))

        return hashlib.sha256("-".join(parts).encode("utf-8")).hexdigest()

    def cache_build_key(self, request: Request, *args, **kwargs) -> str:
        """Build cache key, under which response will be retrieved and saved."""
        assert self.prefix, "{name}.cache_prefix cannot be empty".format(name=self.__class__.__name__)  # noqa: S101
        return "{prefix}-{lang}-{hash}".format(
            prefix=self.prefix, lang=request.LANGUAGE_CODE, hash=self.cache_build_hash(request, *args, **kwargs)
        )

    def cache_get(self, request: Request, *args, **kwargs) -> Optional[Response]:
        """Retrieve response from cache."""
        if not self.prefix:
            return None

        key = self.cache_build_key(request, *args, **kwargs)
        data = self.cache.get(key, b"")
        if data:
            try:
                data = Response(json.loads(data, parse_float=Decimal))
                logger.debug("Cache hit: %s" % request.path)
                return data
            except (TypeError, EOFError) as error:
                self.cache.delete(key)
                capture_exception(error)

    def cache_save(self, response: Response, request: Request, *args, **kwargs):
        """Save response in cache."""
        if not self.prefix:
            return

        if not isinstance(response, Response):
            return

        if response.status_code != 200:
            return

        key = self.cache_build_key(request, *args, **kwargs)
        try:
            self.cache.set(key, json.dumps(response.data, cls=CustomJSONEncoder), timeout=self.timeout)
            logger.debug("Cache saved: %s [timeout=%s]" % (request.path, self.timeout))
        except Exception as error:
            capture_exception(error)

    def cache_clear(self):
        """Clear cache for a given city."""
        for lang in dict(settings.LANGUAGES).keys():
            key = f"{self.prefix}-{lang}-*"
            self.cache.delete_pattern(key)


def cache(prefix, alias=settings.API_CACHE_ALIAS, timeout=settings.API_CACHE_TIMEOUT,) -> CacheDecorator:
    """Returns instance CacheDecorator."""
    return CacheDecorator(prefix, alias, timeout)
