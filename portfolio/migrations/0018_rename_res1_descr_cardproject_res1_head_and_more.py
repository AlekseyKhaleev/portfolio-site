# Generated by Django 4.0.3 on 2022-04-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_rename_image_cardproject_logo_cardproject_res1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardproject',
            old_name='res1_descr',
            new_name='res1_head',
        ),
        migrations.RemoveField(
            model_name='cardproject',
            name='res2_descr',
        ),
        migrations.RemoveField(
            model_name='cardproject',
            name='res3_descr',
        ),
        migrations.AddField(
            model_name='cardproject',
            name='res1_lead',
            field=models.TextField(default='Result1 Description'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='res1_span',
            field=models.TextField(default='Result1 Description'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='res2_head',
            field=models.TextField(default='Result1 Description'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='res2_lead',
            field=models.TextField(default='Result1 Description'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='res2_span',
            field=models.TextField(default='Result1 Description'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='res3_head',
            field=models.TextField(default='Result1 Description'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='res3_lead',
            field=models.TextField(default='Result1 Description'),
        ),
        migrations.AddField(
            model_name='cardproject',
            name='res3_span',
            field=models.TextField(default='Result1 Description'),
        ),
    ]