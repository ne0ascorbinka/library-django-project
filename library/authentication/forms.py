from .models import CustomUser
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)
    first_name = forms.CharField(max_length=20, label='First Name', required=True)
    last_name = forms.CharField(max_length=20, label='Last Name', required=True)
    middle_name = forms.CharField(max_length=20, label='Middle Name', required=False)


