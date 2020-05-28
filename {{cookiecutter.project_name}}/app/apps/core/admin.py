from typing import Dict, List, Tuple, Union

from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from apps.core.models import Tag

TypeFieldSet = List[Tuple[Union[None, str], Dict[str, List[str]]]]  # noqa


class BaseActivityAdmin(TranslationAdmin):
    """Base activity admin."""

    list_display = ["is_active", "created_at", "deleted_at"]
    search_fields = ["name"]
    list_filter = ["is_active"]
    list_per_page = 100
    readonly_fields = ["created_at", "deleted_at"]
    fieldsets: TypeFieldSet = [
        (_("Activity"), {"fields": ["is_active", "created_at", "deleted_at"]}),
    ]


class BaseSlugNameActivityAdmin(BaseActivityAdmin):
    """Base slug and name admin."""

    list_display = ["name", "slug"] + BaseActivityAdmin.list_display
    prepopulated_fields = {"slug": ("name_en",)}
    fieldsets: TypeFieldSet = [
        (None, {"fields": ["name", "slug"]}),
        (_("Activity"), {"fields": ["is_active", "created_at", "deleted_at"]},),
    ]


@admin.register(Tag)
class TagAdmin(SortableAdminMixin, BaseSlugNameActivityAdmin):
    """Tag admin."""

    list_filter = ["is_active"]
