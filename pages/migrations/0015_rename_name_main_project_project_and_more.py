# Generated by Django 4.0.4 on 2022-04-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_main_project_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main_project',
            old_name='name',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project_image',
            old_name='name',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='main_project',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
