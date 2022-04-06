# Generated by Django 4.0.3 on 2022-04-05 11:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_blogproject_date_alter_blogproject_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogproject',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 4, 5, 11, 37, 46, 313539, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogproject',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 4, 5, 11, 37, 46, 313565, tzinfo=utc)),
        ),
    ]
