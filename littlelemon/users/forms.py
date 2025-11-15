from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Default user model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # make email mandatory

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
