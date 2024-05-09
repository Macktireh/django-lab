from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as AuthGroupAdmin
from django.contrib.auth.models import Group as AuthGroup
from django.utils.translation import gettext_lazy as _

from apps.users.forms import UserChangeForm, UserCreationForm
from apps.users.models import Group, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = (
        "email",
        "name",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    list_filter = (
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {"fields": ("name",)},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
    readonly_fields = ("date_joined", "last_login")
    search_fields = (
        "email",
        "name",
    )
    ordering = ("date_joined",)


admin.site.unregister(AuthGroup)


@admin.register(Group)
class GroupAdmin(AuthGroupAdmin):
    pass
