from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUp(UserCreationForm):
     email = forms.EmailField(required=True, help_text='Required')

     class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']

