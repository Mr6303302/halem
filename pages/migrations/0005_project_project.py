# Generated by Django 4.0.4 on 2022-04-25 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_image_project_fimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pages.projects'),
        ),
    ]
