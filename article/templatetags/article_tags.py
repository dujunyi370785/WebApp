# 引入django.template库
from django import template
from django.db.models import Count

# Library方法是与模板相关的方法
register = template.Library()

from article.models import ArticlePost


# 该装饰器表明其下面的代码是自定义的simple_tag类型的标签
@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_articles(user):
    return user.article.count()


# 内含标签
@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by('-created')[:n]
    context = {'latest_articles': latest_articles}
    return context


@register.simple_tag
def most_commented_articles(n=3):
    return ArticlePost.objects.annotate(total_comments=Count('comments').order_by('-total_comments'))[:n]
