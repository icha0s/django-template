from .common import *  # noqa

DEBUG = True
SECRET_KEY = "local"

INSTALLED_APPS.append("rosetta")

CACHES = {
    "default": env.cache(default="redis://127.0.0.1:6379/0"),
    "session": env.cache("CACHE_SESSION_URL", default="redis://127.0.0.1:6379/1"),
}


MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
INSTALLED_APPS.append("debug_toolbar")
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = None
CSRF_COOKIE_SAMESITE = None
