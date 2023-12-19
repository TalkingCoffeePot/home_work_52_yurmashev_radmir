from django import forms
from django.forms import widgets
from main_app.models import TypeModel, StatusModel, Task

# class TaskForm(forms.Form):
#     summery = forms.CharField(max_length=200, required=True, label='Короткое описание')
#     description = forms.CharField(max_length=1500, required=True, label='полное описание',
#                             widget=widgets.Textarea)
#     task_status = forms.ModelChoiceField(queryset=StatusModel.objects.all())
#     task_types = forms.ModelMultipleChoiceField(queryset=TypeModel.objects.all())

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
    
    def clean_tite(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Слишком короткое название")
        return title