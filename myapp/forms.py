from django import forms 
from .models import Visitor,Article
from django.forms import ModelForm
from django.contrib.auth.models import User
import re

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    

    class Meta:
        model = Visitor
        fields = ['username', 'email', 'password', 'confirm_password',
                  'mobile', 'name', 'address','photo']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))                  