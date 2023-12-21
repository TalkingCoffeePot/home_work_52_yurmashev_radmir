from django import forms
from django.forms import widgets
from main_app.models import TypeModel, StatusModel, Task, ProjectModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'summery',
            'description',
            'task_status',
            'task_types',
        ]
    
    def clean_description(self):
        desc = self.cleaned_data['description']
        if 'fuck' in desc:
            raise forms.ValidationError("Нецензурные выражения недопустимы!")
        return desc
    
    def clean_summery(self):
        title = self.cleaned_data['summery']
        if len(title) < 5:
            raise forms.ValidationError("Слишком короткое название")
        return title
    

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = [
            'title',
            'description',
            'date_create',
            'date_finish',
        ]