# Generated by Django 4.0.4 on 2022-04-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_project_alter_projects_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=0, upload_to='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cotente',
            field=models.TextField(max_length=1000),
        ),
    ]
