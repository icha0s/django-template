import datetime

SESSION_CACHE_ALIAS = "session"
SESSION_COOKIE_AGE = int(datetime.timedelta(days=2).total_seconds())
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"
# SESSION_COOKIE_DOMAIN = ""
SESSION_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = True
