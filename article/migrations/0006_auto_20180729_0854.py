# Generated by Django 2.0.5 on 2018-07-29 08:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20180729_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentator', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 29, 8, 54, 29, 311293)),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='article.ArticlePost', verbose_name='评论'),
        ),
    ]
