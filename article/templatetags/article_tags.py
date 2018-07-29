# 引入django.template库
from django import template

# Library方法时与模板相关的方法
register = template.Library()

from article.models import ArticlePost


# 该装饰器表明其下面的代码是自定义的simple_tag类型的标签
@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()
