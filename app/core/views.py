# app/core/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.core.models import Product

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
	return render(request, 'app/core/product_list.html')
