# Generated by Django 2.0.5 on 2018-07-29 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180725_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 29, 8, 53, 12, 950411)),
        ),
    ]
