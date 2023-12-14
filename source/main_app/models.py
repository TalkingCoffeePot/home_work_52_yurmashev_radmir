from django.db import models

# Create your models here.

status_choices = [('new', 'New'), ('in_progress', 'In progress'),  ('done', 'Done')]

class StatusModel(models.Model):
    status = models.CharField('Наименование статуса', max_length=100, null=False, blank=False)

class TypeModel(models.Model):
    type = models.CharField('Тип задачи', max_length=100, null=False, blank=False)

class Task(models.Model):
    summery = models.CharField(max_length=100, null=False, blank=False, verbose_name='Краткое описание')
    description = models.TextField(max_length=1150, null=False, blank=False, verbose_name='Полное описание')
    task_status = models.ForeignKey(StatusModel, related_name='task', on_delete=models.PROTECT)
    task_type = models.ForeignKey(TypeModel, related_name='task', on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.pk}, {self.description}, {self.task_status}, {self.date}' 