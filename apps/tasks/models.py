from typing import Any, override

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify


class Task(models.Model):
    title = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(5)])
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tasks"
        ordering = ["-created"]

    @override
    def save(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
