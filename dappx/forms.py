# dappx/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from dappx.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.Form):
    upload_file = forms.FileField()