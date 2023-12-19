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
from django.urls import path
from main_app.views import MainView, TaskView, AddTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='tasks'),
    path('tasks/new/', AddTaskView.as_view(), name='new_task'),
    path('tasks/<int:task_pk>/', TaskView.as_view(), name='task_details'),
    path('tasks/<int:task_pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('tasks/<int:task_pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]
