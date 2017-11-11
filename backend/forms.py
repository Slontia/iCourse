from django import forms
import re
from django.contrib.auth.models import User
from .models import Resource

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password1 = forms.CharField(required=True, max_length=20)
    password2 = forms.CharField(required=True, max_length=20)
    email = forms.EmailField(required=True, max_length=254)
    nickname = forms.CharField(required=False, max_length=20)
    gender = forms.CharField(required=False, max_length=20)
    intro = forms.CharField(required=False, max_length=254)

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
    
    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if(gender != '1' and gender != '2' and gender != '0'):    # '1':男 '2':女 '0':保密
            raise forms.ValidationError("性别错误")
        return gender   


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, max_length=20)


class ResourceUploadForm(forms.ModelForm):
    class Meta:
        model =  Resource
        fields =  ['name', 'size', 'upload_user_id','course_code']
    
    def clean_size(self):
        # 2.5MB - 2621440
        # 5MB - 5242880
        # 10MB - 10485760
        # 20MB - 20971520
        # 50MB - 52428800
        # 100MB - 104857600
        # 250MB - 214958080
        # 500MB - 429916160
        MAX_UPLOAD_SIZE = "10485760"
        size = int(self.cleaned_data['size'])
        if(size > int(MAX_UPLOAD_SIZE)):
            raise forms.ValidationError("文件不能超过10MB")
        return size


class UserInfoModifyForm(forms.Form):
    nickname = forms.CharField(required=False, max_length=20)
    gender = forms.CharField(required=False, max_length=20)
    intro = forms.CharField(required=False, max_length=100)
    college_id = forms.IntegerField(required=False)

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if(gender != '1' and gender != '2' and gender != '0'):    # '1':男 '2':女 '0':保密
            raise forms.ValidationError("性别错误")
        return gender

    def clean_college_id(self):
        college_id = int(self.cleaned_data['college_id'])
        if(college_id <= 0):
            raise forms.ValidationError("学院错误")
        return college_id
