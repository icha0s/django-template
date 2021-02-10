from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.utils.translation import gettext_lazy as _

from apps.account import models


class UserChangeForm(BaseUserChangeForm):
    """User change form."""

    class Meta(BaseUserChangeForm.Meta):
        model = models.User


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """User admin."""

    form = UserChangeForm
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "created_at",
        "joined_at",
        "deleted_at",
    )
    search_fields = ("username", "first_name", "last_name", "email")
    list_filter = ("is_active",)
    list_per_page = 100
    readonly_fields = ("created_at", "joined_at", "deleted_at")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email", "first_name", "last_name", "language",)},),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Activity"), {"fields": ("created_at", "joined_at", "deleted_at")},),
    )
