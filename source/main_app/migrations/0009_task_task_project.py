# Generated by Django 4.2.7 on 2023-12-21 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_projectmodel_date_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='project', to='main_app.projectmodel'),
        ),
    ]
