import os

from django.utils.translation import gettext_lazy as _

from ..common import BASE_DIR

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "uk"
LANGUAGES = (
    ("en", _("English")),
    ("uk", _("Ukrainian")),
    ("ru", _("Russian")),
)
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale/")]

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True
