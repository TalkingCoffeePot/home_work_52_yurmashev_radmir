from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import DeleteView,  UpdateView, CreateView
from main_app.models import Task, ProjectModel
from main_app.forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AddTaskView(PermissionRequiredMixin, CreateView):    
    template_name = 'tasks/add_task.html'
    form_class = TaskForm
    permission_required = 'main_app.create_tasks'

    def form_valid(self, form):
        project = get_object_or_404(ProjectModel, pk=self.kwargs.get('project_pk'))
        task = form.save(commit=False)
        task.task_project = project
        task.save()
        return redirect('project_details', project_pk=project.pk)
    


class UpdateTaskView(PermissionRequiredMixin, UpdateView):
    template_name = 'tasks/update_task.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'
    pk_url_kwarg = 'task_pk'
    permission_required = 'main_app.change_tasks'

    def get_success_url(self):
        return reverse('project_details', kwargs={'project_pk': self.object.task_project.pk})

    

class DeleteTaskView(PermissionRequiredMixin, DeleteView):
    template_name = 'tasks/delete_task.html'
    model = Task
    context_object_name = 'task'
    pk_url_kwarg = 'task_pk'
    permission_required = 'main_app.delete_tasks'

    def get_success_url(self):
        return reverse('project_details', kwargs={'project_pk': self.object.task_project.pk})
    
    

