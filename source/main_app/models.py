from django.db import models
from main_app.validators import clean_description, clean_tite

# Create your models here.

status_choices = [('new', 'New'), ('in_progress', 'In progress'),  ('done', 'Done')]

class StatusModel(models.Model):
    status = models.CharField('Наименование статуса', max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.status}'
    

class TypeModel(models.Model):
    type = models.CharField('Тип задачи', max_length=100, null=False, blank=False)
 
    def __str__(self):
        return f'{self.type}'
    

class Task(models.Model):
    summery = models.CharField(max_length=100, null=False, blank=False, verbose_name='Краткое описание', validators=[clean_tite])
    description = models.TextField(max_length=1150, null=False, blank=False, verbose_name='Полное описание', validators=[clean_description])
    task_status = models.ForeignKey(StatusModel, related_name='task', on_delete=models.PROTECT)
    task_types = models.ManyToManyField('main_app.TypeModel', related_name='task_set', blank=True)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.pk}, {self.summery}, {self.task_status}, {self.date_update}' 