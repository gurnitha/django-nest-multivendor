# app/userauth/urls.py

# Django modules
from django.urls import path

# Locals
from app.userauth import views 

app_name = 'userauth'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]