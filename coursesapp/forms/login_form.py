from django.contrib.auth import forms, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms import ValidationError

class LoginForm(AuthenticationForm):

    username = forms.CharField(max_length=100, required=True, label="AAP ROLL")
    
