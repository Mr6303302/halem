# Generated by Django 4.0.4 on 2022-04-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_alter_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_project',
            name='cotente',
            field=models.TextField(default=0, max_length=1000),
        ),
    ]
