from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UserConfig(AppConfig):
    """User application."""

    name = "apps.accounts"
    verbose_name = _("Accounts")
