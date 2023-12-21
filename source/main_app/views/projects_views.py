from typing import Any
from django.db.models.query import QuerySet
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from main_app.models import ProjectModel
from main_app.forms import ProjectForm
from django.urls import reverse

class ListProjectsView(ListView):
    template_name = 'projects/list_project.html'
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 1
    
    def get_queryset(self) -> QuerySet[Any]:
        return ProjectModel.objects.all()
    

class DetailProjectView(DeleteView):
    template_name = 'projects/detailed_project.html'
    model = ProjectModel
    context_object_name = 'project'
    pk_url_kwarg = 'project_pk'


class CreateProjectView(CreateView):
    template_name = 'projects/create_project.html'
    form_class = ProjectForm
    
    def get_success_url(self):
        return reverse('projects')