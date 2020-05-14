from .common import *  # noqa

DEBUG = True
SECRET_KEY = "local"

CACHES = {
    "default": env.cache(default="redis://127.0.0.1:6379/0"),
    "session": env.cache("CACHE_SESSION_URL", default="redis://127.0.0.1:6379/1"),
}
