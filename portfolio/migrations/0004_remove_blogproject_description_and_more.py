# Generated by Django 4.0.3 on 2022-03-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_blogproject_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogproject',
            name='description',
        ),
        migrations.AlterField(
            model_name='blogproject',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
