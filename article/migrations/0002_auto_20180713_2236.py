# Generated by Django 2.0.5 on 2018-07-13 22:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 7, 13, 22, 36, 0, 644326))),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='article', to=settings.AUTH_USER_MODEL)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='article_column', to='article.ArticleColumn')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterIndexTogether(
            name='articlepost',
            index_together={('id', 'slug')},
        ),
    ]