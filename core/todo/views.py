from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View

from todo.forms import TaskUpdateForm
from .models import Task


# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    """
    CBV for listing user tasks
    """

    model = Task
    context_object_name = "tasks"
    template_name = "todo/todo_list.html"

    def get_queryset(self):

        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    a CBV for creating new task in todo app
    """

    model = Task
    fields = ("title",)
    success_url = reverse_lazy("todo-list")
    template_name = "todo/todo_create.html"
    # form_class = TaskForm      # it could be, it's not wrong

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  # do we really need to give super() values??



class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    updated task based on TaskUpdateForm and redirects to list of tasks 
    """
    model = Task
    success_url = reverse_lazy("task-list")
    form_class = TaskUpdateForm
    template_name = "todo/update_task.html"
    


class TaskCompleteView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("task-list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True 
        object.save()
        return redirect(self.success_url)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Deletes Task and redirects to list of tasks(makes sure that users only delete their own tasks)
    """
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("task-list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)