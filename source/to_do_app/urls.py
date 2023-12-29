from django.contrib import admin
from django.urls import path, include
from main_app.views import  AddTaskView, UpdateTaskView, DeleteTaskView
from main_app.views import ListProjectsView, DetailProjectView, CreateProjectView, UpdateProject, DeleteProject


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
