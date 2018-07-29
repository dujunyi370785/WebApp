from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth = models.DateField('出生日期', blank=True, null=True)
    phone = models.CharField('联系电话', max_length=20, null=True)
    profession = models.CharField('职业', max_length=20, null=True)


    def __str__(self):
        return 'user {}'.format(self.user.username)