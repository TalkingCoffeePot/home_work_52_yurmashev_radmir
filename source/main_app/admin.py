from django.contrib import admin
from django import forms
from main_app.models import Task, StatusModel, TypeModel, ProjectModel
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
@admin.register(StatusModel)
class StatusModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_editable = ['status']

@admin.register(TypeModel)
class TypeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_editable = ['type']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['summery', 
                    'description',
                    'task_status', 
                    'date_create', 
                    'date_update',]
    

@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'description',
        'date_create',
        'date_finish',
    ]


