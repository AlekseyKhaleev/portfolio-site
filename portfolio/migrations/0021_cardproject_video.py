# Generated by Django 4.0.3 on 2022-04-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_cardproject_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardproject',
            name='video',
            field=models.FileField(default='video', upload_to='portfolio/docs/'),
        ),
    ]