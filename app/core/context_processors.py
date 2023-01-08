# app/core/context_processor.py

# Locals
from app.core.models import Category

def default(request):
	cat_values = Category.objects.all()[0:5]
	cat_values2 = Category.objects.all()[5:10]
	print(cat_values)
	print(cat_values2)
	return {
		'cat_keys': cat_values,
		'cat_keys2': cat_values2,
	}