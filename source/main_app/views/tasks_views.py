from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, TemplateView, FormView
from main_app.models import Task
from main_app.forms import TaskForm



class MainView(TemplateView):
    template_name='tasks/main_page.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['tasks'] = Task.objects.all()
        return super().get_context_data(**kwargs)
    

class AddTaskView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {
        'form': form
        }
        return render(request, 'tasks/add_task.html', context)
    
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


class UpdateTaskView(FormView):
    template_name = 'tasks/update_task.html'
    form_class = TaskForm

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['task'] = self.task
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form: Any) -> HttpResponse:
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('task_details', kwargs={'task_pk': self.task.pk})

    def get_object(self):
        pk=self.kwargs.get('task_pk')
        return get_object_or_404(Task, pk=pk)



class DeleteTaskView(TemplateView):
    template_name = 'delete_task.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
        return super().get_context_data(**kwargs)
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['task_pk']) 
        task.delete()
        return redirect('tasks')  



class TaskView(TemplateView):
    template_name = 'tasks/detailed_task.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        kwargs['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
        return super().get_context_data(**kwargs)