# Generated by Django 4.0.4 on 2022-04-25 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_main_project_rename_fimage_project_image_and_more'),
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