from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.core.models import CreatedDeletedModel


class User(AbstractBaseUser, PermissionsMixin, CreatedDeletedModel):
    """User model."""

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[UnicodeUsernameValidator()],
        error_messages={"unique": _("A user with that username already exists.")},
    )
    first_name = models.CharField(_("First name"), max_length=30, blank=True)
    last_name = models.CharField(_("Last name"), max_length=150, blank=True)
    email = models.EmailField(_("Email"), blank=True)
    is_staff = models.BooleanField(_("Staff status"), default=False)
    is_active = models.BooleanField(_("Is active?"), default=True)
    joined_at = models.DateTimeField(_("Joined at"), default=timezone.now)
    language = models.CharField(_("Language"), max_length=2, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def clean(self):
        """Extra model-wide validation."""
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        if self.first_name or self.last_name:
            return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name).strip()
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        swappable = "AUTH_USER_MODEL"
        db_table = "users"
