# app/core/urls.py

# Django modules
from django.urls import path

# Locals
from app.core import views 

app_name = 'core'

urlpatterns = [

    # Homepage
    path('', views.index, name='index'),
    path('products/', views.product_list_view, name='product_list_view'),
    path('product-detail/<any>/', views.product_detail_view, name='product_detail_view'),

    # Category
    path('categories/', views.category_list_view, name='category_list_view'),
    path('category/<cat_id>/', views.product_by_category_list_view, name='product_by_category_list_view'),

    # Vendor
    path('vendors/', views.vendor_list_view, name='vendor_list_view'),
    path('vendor/<vid>', views.vendor_detail_view, name='vendor_detail_view'),
]
