from django.db import models
from django.contrib.auth.models import User
from .articlepost import ArticlePost


class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, related_name='comments', on_delete=models.DO_NOTHING, verbose_name='评论')
    commentator = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {0} on {1}'.format(self.commentator.username, self.article)