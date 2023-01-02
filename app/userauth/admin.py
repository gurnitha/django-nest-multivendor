# app/userauth/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.userauth.models import User 

# Register your models here.

# Customising user display in admin panel
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'bio']
	
admin.site.register(User, UserAdmin)