# Generated by Django 4.0.4 on 2022-04-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_main_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
