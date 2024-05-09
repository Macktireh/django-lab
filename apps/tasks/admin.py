from django.contrib import admin

from apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "completed",
        "created",
        "updated",
    )
    list_filter = (
        "completed",
        "created",
        "updated",
    )
    search_fields = (
        "title",
        "description",
    )
    prepopulated_fields = {"slug": ("title",)}
