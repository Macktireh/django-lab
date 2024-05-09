from django.forms import ModelForm, Textarea, TextInput

from apps.tasks.models import Task


class TaskForm(ModelForm):
    """Form definition for Task."""

    class Meta:
        model = Task
        fields = ["title", "description", "completed"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
        }
