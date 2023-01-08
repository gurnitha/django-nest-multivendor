# app/core/context_processor.py

# Locals
from app.core.models import Category

def default(request):
	cat_values = Category.objects.all()
	print(cat_values)
	return {
		'cat_keys': cat_values,
	}