from django import forms
from .models import Yangilik
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']


class YangilikForm(forms.ModelForm):
    class Meta:
        model = Yangilik
        fields = "__all__"