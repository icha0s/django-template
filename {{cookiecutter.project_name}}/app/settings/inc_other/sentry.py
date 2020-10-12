import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

from ..common import DEBUG  # noqa
from ..common import env  # noqa

sentry_sdk.init(
    env.str("SENTRY_DSN", ""),
    debug=DEBUG,
    environment=env.str("SENTRY_ENV", ""),
    release=env.str("SENTRY_RELEASE", "1.0.1"),
    integrations=[CeleryIntegration(), DjangoIntegration()],
)
