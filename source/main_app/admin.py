from django.contrib import admin
from main_app.models import Task, StatusModel, TypeModel
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
    list_display = ['id', 
                    'summery', 
                    'description', 
                    'task_status', 
                    'task_type', 
                    'date_create', 
                    'date_update']
    
    list_editable = ['summery', 
                    'description', 
                    'task_status', 
                    'task_type',]

    def edit_link(self, obj):
        current_url = reverse('admin:main_app_task_change', args=[obj.id])
        return format_html('<a href="{}">Edit</a>', current_url)
    
    edit_link.short_description = 'Редактирование'
    edit_link.allow_tags = True
