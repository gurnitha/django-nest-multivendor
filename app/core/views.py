# app/core/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.core.models import Product, Category, Vendor

# Create your views here.

# Homepage
def index(request):
	# products = Product.objects.all().order_by('-id')
	products = Product.objects.filter(status_choice='published', featured=True)
	# print(products)
	context = {
		'products':products,
	}
	return render(request, 'app/core/index.html', context)


# Product List
def product_list_view(request):
	products = Product.objects.all()
	# print(products)
	context = {'products':products}
	return render(request, 'app/core/product_list.html', context)


# Category List
def category_list_view(request):
	categories = Category.objects.all()
	# print(categories)
	context = {'categories':categories}
	return render(request, 'app/core/category_list.html', context)


# Product By Category
def product_by_category_list_view(request, cat_id):
	category_based_id = Category.objects.get(cid=cat_id)
	products = Product.objects.filter(status_choice='published', category=category_based_id)
	context = {
		'category': category_based_id,
		'products': products,
	}
	return render(request, 'app/core/product_by_category_list.html', context)


# Vendor List
def vendor_list_view(request):
	context = {
	}
	return render(request, 'app/core/vendor_list.html', context)
