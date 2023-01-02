# app/userauth/forms.py

# Django modules
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Locals
from app.userauth.models import User 


# UserRegisterForm
class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User 
		fields = ['username', 'email']