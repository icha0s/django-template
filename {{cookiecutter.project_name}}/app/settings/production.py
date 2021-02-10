from .common import *  # noqa

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    "rest_framework.renderers.JSONRenderer",
]

API_CACHE_TIMEOUT = 60 * 60 * 24
SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")
