from typing import Any
from urllib.parse import urlencode
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from main_app.models import ProjectModel
from main_app.forms import ProjectForm, SimpleSearchForm, ProjectUsersForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ListProjectsView(ListView):
    template_name = 'projects/list_project.html'
    context_object_name = 'projects'
    model = ProjectModel
    paginate_by = 5
    paginate_orphans = 1
    
    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None
    

class DetailProjectView(DetailView):
    template_name = 'projects/detailed_project.html'
    model = ProjectModel
    context_object_name = 'project'
    pk_url_kwarg = 'project_pk'
    


class CreateProjectView(PermissionRequiredMixin, CreateView):
    template_name = 'projects/create_project.html'
    form_class = ProjectForm
    permission_required = 'main_app.create_projects'
    
    def get_success_url(self):
        return reverse('projects')
    

class UpdateProject(PermissionRequiredMixin, UpdateView):
    model = ProjectModel
    template_name = 'projects/update_project.html'
    pk_url_kwarg = 'project_pk'
    form_class = ProjectForm
    context_object_name = 'project'
    permission_required = 'main_app.change_projects'

    def get_success_url(self):
        return reverse('project_details', kwargs={'project_pk': self.object.pk})
    

class DeleteProject(LoginRequiredMixin, DeleteView):
    template_name = 'projects/delete_project.html'
    pk_url_kwarg = 'project_pk'
    model = ProjectModel
    context_object_name = 'project'
    success_url = reverse_lazy('projects')
    permission_required = 'main_app.delete_projects'

class UpdateProjectUsers(PermissionRequiredMixin, UpdateView):
    model = ProjectModel
    template_name = 'projects/user_update.html'
    pk_url_kwarg = 'project_pk'
    form_class = ProjectUsersForm
    context_object_name = 'project'
    permission_required = 'main_app.change_users'

    def get_success_url(self):
        return reverse('project_details', kwargs={'project_pk': self.object.pk})