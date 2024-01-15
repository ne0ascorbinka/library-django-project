from typing import Any
from .models import CustomUser
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm password', required=True)
    first_name = forms.CharField(max_length=20, label='First Name', required=True)
    last_name = forms.CharField(max_length=20, label='Last Name', required=True)
    middle_name = forms.CharField(max_length=20, label='Middle Name', required=False)

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords don't match")
        
        return cleaned_data


