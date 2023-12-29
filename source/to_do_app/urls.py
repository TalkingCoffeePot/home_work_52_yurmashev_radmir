"""
URL configuration for to_do_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app.views import  AddTaskView, UpdateTaskView, DeleteTaskView
from main_app.views import ListProjectsView, DetailProjectView, CreateProjectView, UpdateProject, DeleteProject
from accounts.views import login_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView

app_name='main_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListProjectsView.as_view(), name='projects'),
    path('projects/<int:project_pk>', DetailProjectView.as_view(), name='project_details'),
    path('projects/create/', CreateProjectView.as_view(), name='create_project'),
    path('projects/<int:project_pk>/update/', UpdateProject.as_view(), name='update_project'),
    path('projects/<int:project_pk>/delete/', DeleteProject.as_view(), name ='delete_project'),

    path('projects/<int:project_pk>/tasks/new/', AddTaskView.as_view(), name='new_task'),
    path('projects/<int:project_pk>/tasks/<int:task_pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('projects/<int:project_pk>/tasks/<int:task_pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
    path('accounts/', include('accounts.urls'))
]
