from django import forms
from account.models import UserProfile, UserInfo


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme')
