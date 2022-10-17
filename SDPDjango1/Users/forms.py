from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #firstname = forms.Name()
   # lastname = forms.Name()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
