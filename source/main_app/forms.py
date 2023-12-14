from django import forms
from django.forms import widgets
from main_app.models import TypeModel, StatusModel

class TaskForm(forms.Form):
    summery = forms.CharField(max_length=200, required=True, label='Короткое описание')
    description = forms.CharField(max_length=1500, required=True, label='полное описание',
                            widget=widgets.Textarea)
    task_status = forms.ModelChoiceField(queryset=StatusModel.objects.all())
    task_type = forms.ModelChoiceField(queryset=TypeModel.objects.all())
  
    
    