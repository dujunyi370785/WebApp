from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    # 内部类
    class Meta:
        # 表单类所应用的数据模型
        model = User
        fields = ('username', 'email')

    # 检验用户所输入的两个密码是否一致，当调用is_valid()方法时被执行
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password do not match')

        return cd['password']