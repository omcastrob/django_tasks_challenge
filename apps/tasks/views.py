from typing import Dict
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm

from apps.tasks.models import Task


class MyTasksView(LoginRequiredMixin, TemplateView):
    template_name = "tasks/my_tasks.html"

    def get_context_data(self, **kwargs) -> Dict:
        context = super().get_context_data(**kwargs)

        tasks = Task.objects.filter(user=self.request.user).order_by('-created_at')
        context.update({
            'tasks': tasks,
        })

        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('my-tasks')
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('my-tasks')
    form_class = TaskForm
    model = Task

    def get_queryset(self):
        # Only allow the user to edit their own tasks
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('my-tasks')
    model = Task

    def get_queryset(self):
        # Only allow the user to delete their own tasks
        return Task.objects.filter(user=self.request.user)
