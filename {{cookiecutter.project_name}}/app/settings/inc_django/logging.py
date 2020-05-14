LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"default": {"format": "[%(asctime)s] [%(levelname)8s]: %(message)s"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "default", "level": "DEBUG"}},
    "loggers": {
        "django": {"handlers": ["console"], "level": "WARNING"},
        "api": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        "apps": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        "api_cache": {"handlers": ["console"], "level": "INFO", "propagate": False},
    },
}
