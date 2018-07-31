from django.db import models
from django.contrib.auth.models import User


class ArticleTag(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='tag')
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag
