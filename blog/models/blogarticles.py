from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogArticles(models.Model):
    # 字段的最大长度为300
    title = models.CharField(max_length=300)
    # 博客与用户之间的关系为一对多
    # related_name的作用是允许通过类User反向查询到BlogArticles
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING)
    # 博客的主体内容
    content = models.TextField()
    # 发布时间
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish", )

    def __str_(self):
        return self.title
