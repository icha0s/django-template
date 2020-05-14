from ..common import DEBUG

# https://github.com/jazzband/django-debug-toolbar
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "settings.inc_other.debug_toolbar.show_toolbar",
}


def show_toolbar(request):
    """Function returns toolbar should show or not."""
    return DEBUG
