# Generated by Django 4.0.4 on 2022-04-25 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_image',
            name='project',
        ),
        migrations.DeleteModel(
            name='main_project',
        ),
        migrations.DeleteModel(
            name='project',
        ),
        migrations.DeleteModel(
            name='project_image',
        ),
    ]
