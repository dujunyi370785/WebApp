# Generated by Django 2.0.5 on 2018-07-25 21:15

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_auto_20180716_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-created', 'title')},
        ),
        migrations.AddField(
            model_name='articlepost',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='article_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 25, 21, 15, 50, 372658)),
        ),
    ]
