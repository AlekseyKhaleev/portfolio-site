# Generated by Django 4.0.3 on 2022-04-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_rename_res1_descr_cardproject_res1_head_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardproject',
            name='description',
        ),
        migrations.AddField(
            model_name='cardproject',
            name='description_head',
            field=models.TextField(default='Description Head'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='description_lead',
            field=models.TextField(default='Description Lead'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='description_span',
            field=models.TextField(default='Description Span'),
        ),
        migrations.AlterField(
            model_name='cardproject',
            name='title',
            field=models.TextField(default='Title'),
        ),
    ]
