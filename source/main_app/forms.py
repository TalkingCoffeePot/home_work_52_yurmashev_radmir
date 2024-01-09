from django import forms
from main_app.models import Task, ProjectModel

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

class ProjectUsersForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['users']

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")