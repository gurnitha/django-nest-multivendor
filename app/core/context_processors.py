# app/core/context_processor.py

# Locals
from app.core.models import Category, Address

def default(request):
	categories = Category.objects.all()
	cat_values = Category.objects.all()[0:5]
	cat_values2 = Category.objects.all()[5:10]
	cat_values3 = Category.objects.all()[4:6]
	cat_values4 = Category.objects.all()[6:7]
	# print(cat_values)
	# print(cat_values2)
	# print(cat_values3)
	# print(cat_values4)
	# Get the address who ever logged in
	# address = Address.objects.get(user=request.user)
	# print(address)
	return {
		'categories': categories,
		'cat_keys': cat_values,
		'cat_keys2': cat_values2,
		'cat_keys3': cat_values3,
		'cat_keys4': cat_values4,
		# 'address':address,
	}