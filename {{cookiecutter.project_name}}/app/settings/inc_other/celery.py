from ..common import env

CELERY_BROKER_URL = env("CELERY_BROKER_URL", str, "redis://redis/14")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", str, "redis://redis/15")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = env("TIME_ZONE", str, "Europe/Kiev")
CELERYBEAT_SCHEDULE = {}
