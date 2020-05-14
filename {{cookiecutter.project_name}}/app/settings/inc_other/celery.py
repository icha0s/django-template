import os

from ..common import env

BROKER_URL = os.environ.get(env.DEFAULT_CACHE_ENV, "redis://redis/14")
CELERY_RESULT_BACKEND = os.environ.get(env.DEFAULT_CACHE_ENV, "redis://redis/15")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = env("TIME_ZONE", str, "Europe/Kiev")
CELERYBEAT_SCHEDULE = {}
