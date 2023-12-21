# Generated by Django 4.2.7 on 2023-12-21 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_task_task_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodel',
            name='date_update',
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='date_finish',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='date_create',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
