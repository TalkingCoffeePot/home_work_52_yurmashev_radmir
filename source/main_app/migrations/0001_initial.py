# Generated by Django 4.2.7 on 2023-12-14 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, verbose_name='Наименование статуса')),
            ],
        ),
        migrations.CreateModel(
            name='TypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Тип задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summery', models.CharField(max_length=100, verbose_name='Краткое описание')),
                ('description', models.TextField(max_length=1150, verbose_name='Полное описание')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('task_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task', to='main_app.statusmodel')),
                ('task_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task', to='main_app.typemodel')),
            ],
        ),
    ]
