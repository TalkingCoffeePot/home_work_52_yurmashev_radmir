from django import forms
from django.forms import widgets

# class TaskForm(forms.Form):
#     description = forms.CharField(max_length=200, required=True, label='Задача')
#     task_status = forms.ChoiceField(choices=status_choices)
#     date = forms.CharField(max_length=10, required=True, label='Сделать до...(YYYY-MM-DD)')
#     details = forms.CharField(max_length=1500, required=True, label='Детали задачи',
#                            widget=widgets.Textarea)
    