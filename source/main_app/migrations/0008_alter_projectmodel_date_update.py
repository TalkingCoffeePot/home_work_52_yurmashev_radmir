# Generated by Django 4.2.7 on 2023-12-21 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_projectmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='date_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
    ]