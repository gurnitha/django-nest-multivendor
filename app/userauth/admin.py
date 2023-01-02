# app/userauth/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.userauth.models import User 

# Register your models here.
admin.site.register(User)
	
