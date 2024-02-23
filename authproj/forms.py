from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from .models import *

class RegistationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'phone', 'password1', 'password2']

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['phone', 'password']