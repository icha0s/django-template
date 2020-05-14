from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    """Application  Core."""

    name = "apps.core"
    verbose_name = _("Core")
