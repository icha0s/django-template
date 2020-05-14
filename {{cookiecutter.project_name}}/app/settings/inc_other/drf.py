# https://github.com/encode/django-rest-framework

REST_FRAMEWORK = {
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        # "apps.core.authentication.JWTAuthentication",
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
    "DEFAULT_THROTTLE_RATES": {"anon": "100/min", "user": "200/min"},
    "COERCE_DECIMAL_TO_STRING": False,
    "EXCEPTION_HANDLER": "apps.core.exceptions.exception_handler",
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S.%f%z",
}
