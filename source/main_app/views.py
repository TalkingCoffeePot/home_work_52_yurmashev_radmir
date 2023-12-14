from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, TemplateView
from main_app.models import Task
from main_app.forms import TaskForm



class MainView(TemplateView):
    template_name='main_page.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['tasks'] = Task.objects.all()
        return super().get_context_data(**kwargs)
    

class AddTaskView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {
        'form': form
        }
        return render(request, 'add_task.html', context)
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('task_types')
            task = Task.objects.create(summery=form.cleaned_data['summery'],
                                description=form.cleaned_data['description'], 
                                task_status=form.cleaned_data['task_status']
                                )
            task.task_types.set(types)             
            return redirect('task_details', task_pk=task.pk)
        else:
            return render(request, 'new_task', context={'form': form})

class UpdateTaskView(View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['task_pk']) 
        form = TaskForm(initial={
                'summery': task.summery,
                'description': task.description,
                'task_status': task.task_status,
                'task_type': task.task_types.all()
            })
        context = {
                'task': task,
                'form': form
            }
        return render(request, 'update_task.html', context)
    
    def post(self, request, *args, **kwargs):
            form = TaskForm(data=request.POST)
            task = Task.objects.get(pk=kwargs['task_pk']) 
            if form.is_valid():
                types = form.cleaned_data.pop('task_types')
                task.summery = form.cleaned_data['summery']
                task.description = form.cleaned_data['description']
                task.task_status = form.cleaned_data['task_status']
                task.save()
                task.task_types.set(types)       
                return redirect('task_details', task_pk=task.pk)
            else:
                return render(request, 'update_task', context={'task': task,'form': form})

class DeleteTaskView(TemplateView):
    template_name = 'delete_task.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
        return super().get_context_data(**kwargs)
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['task_pk']) 
        task.delete()
        return redirect('tasks')  
# def delete_task(request, pk):
#     task = Task.objects.get(pk=pk) 
#     if request.method == 'GET':
#         return render(request, 'delete_task.html', context={'task': task})
#     elif request.method == 'POST':
#         task.delete()
#         return redirect('tasks')    


class TaskView(TemplateView):
    template_name = 'detailed_task.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
        return super().get_context_data(**kwargs)