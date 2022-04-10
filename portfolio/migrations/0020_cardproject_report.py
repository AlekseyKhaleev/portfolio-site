# Generated by Django 4.0.3 on 2022-04-10 16:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_remove_cardproject_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardproject',
            name='report',
            field=models.FileField(default=django.utils.timezone.now, upload_to='portfolio/docs/'),
            preserve_default=False,
        ),
    ]