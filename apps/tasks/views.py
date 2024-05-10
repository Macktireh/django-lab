from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django_view_decorator import namespaced_decorator_factory
from djstripe.models import Product

from apps.tasks.forms import TaskForm
from apps.tasks.models import Task

routes = namespaced_decorator_factory(namespace="tasks")


@routes(paths="", name="index")
class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "tasks": Task.objects.all(),
            "completed_tasks": Task.objects.filter(completed=True),
        }
        return render(request, "tasks/index.html", context)


@routes(paths="tasks/create", name="create")
class CreateTaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": TaskForm(),
        }
        return render(request, "tasks/create.html", context)

    def post(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully")
            return redirect("tasks:index")
        return render(request, "tasks/create.html", {"form": form})


@routes(paths="tasks/<str:slug>/completed", name="completed")
class CompleteTaskView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        task = get_object_or_404(Task, slug=slug)
        task.completed = not task.completed
        task.save()
        messages.success(request, "Task completed successfully")
        return redirect("tasks:index")


@routes(paths="tasks/<str:slug>/update", name="update")
class UpdateTaskView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        task = get_object_or_404(Task, slug=slug)
        context = {
            "form": TaskForm(instance=task),
        }
        return render(request, "tasks/update.html", context)

    def post(self, request: HttpRequest, slug: str) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        task = get_object_or_404(Task, slug=slug)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully")
            return redirect("tasks:index")
        return render(request, "tasks/update.html", {"form": form})


@routes(paths="tasks/<str:slug>/delete", name="delete")
class DeleteTaskView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        task = get_object_or_404(Task, slug=slug)
        task.delete()
        messages.success(request, "Task deleted successfully")
        return redirect("tasks:index")


@routes(paths="pricing", name="pricing")
class PricingView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "products": Product.objects.all().order_by("created"),
        }
        return render(request, "tasks/pricing.html", context)
