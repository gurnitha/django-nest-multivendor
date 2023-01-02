# app/userauth/urls.py

# Django modules
from django.urls import path

# Locals
from app.userauth import views 

app_name = 'userauth'

urlpatterns = [
    path('sign-up/', views.register_view, name='sign_up'),
]