# app/userauth/forms.py

# Django modules
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Locals
from app.userauth.models import User 


# UserRegisterForm
class UserRegisterForm(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Emaiil'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))

	class Meta:
		model = User 
		fields = ['username', 'email']