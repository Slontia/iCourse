from django import forms
import re
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password1 = forms.CharField(required=True, max_length=20)
    password2 = forms.CharField(required=True, max_length=20)
    email = forms.EmailField(required=True, max_length=20)
    nickname = forms.CharField(required=False, max_length=20)
    gender = forms.CharField(required=False, max_length=20)
    intro = forms.CharField(required=False, max_length=100)

    def clean_username(self):
        username = self.cleaned_data['username']
        filterResult = User.objects.filter(username=username)
        if(len(filterResult) > 0):
            raise forms.ValidationError("该用户名已被注册")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        search = re.search('@buaa.edu.cn$', email)
        if(search is None):
            raise forms.ValidationError("注册邮箱不是北航邮箱")
        filterResult = User.objects.filter(email=email)
        if(len(filterResult) > 0):
            raise forms.ValidationError("该邮箱已被注册")
        return email
    
    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        password1 = self.cleaned_data['password1']
        if(password2 != password1):
            raise forms.ValidationError("两次输入的密码不一致")
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, max_length=20)

