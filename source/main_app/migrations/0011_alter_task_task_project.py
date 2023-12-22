# Generated by Django 4.2.7 on 2023-12-21 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_remove_projectmodel_date_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='main_app.projectmodel'),
        ),
    ]
