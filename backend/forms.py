from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password1 = forms.CharField(required=True, max_length=20)
    password2 = forms.CharField(required=True, max_length=20)
    email = forms.EmailField(required=True, max_length=20)
    nickname = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=20)
    intro = forms.CharField(max_length=100)
