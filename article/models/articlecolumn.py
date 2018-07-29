from django.db import models
from django.contrib.auth.models import User

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column', on_delete=models.DO_NOTHING)
    column = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.column