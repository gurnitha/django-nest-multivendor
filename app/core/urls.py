# app/core/urls.py

# Django modules
from django.urls import path

# Locals
from app.core import views 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list_view, name='product_list_view'),
]
