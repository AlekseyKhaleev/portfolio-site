# Generated by Django 4.0.3 on 2022-03-27 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_project_blogproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogproject',
            name='image',
        ),
    ]
