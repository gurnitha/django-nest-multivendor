# app/core/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.core.models import Product, Category

# Create your views here.

def index(request):
	# products = Product.objects.all().order_by('-id')
	products = Product.objects.filter(status_choice='published', featured=True)
	# print(products)
	context = {
		'products':products,
	}
	return render(request, 'app/core/index.html', context)


def product_list_view(request):
	products = Product.objects.all()
	# print(products)
	context = {'products':products}
	return render(request, 'app/core/product_list.html', context)


def category_list_view(request):
	categories = Category.objects.all()
	# print(categories)
	context = {'categories':categories}
	return render(request, 'app/core/category_list.html', context)

def product_belong_to_a_category_list_view(request, cat_id):
	return render(request, 'app/core/product_belong_to_a_category_list.html')


