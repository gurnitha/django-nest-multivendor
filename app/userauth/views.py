# app/userauth/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.userauth.forms import UserRegisterForm

# Create your views here.

def register_view(request):
	# Use the UserRegisterForm
	form = UserRegisterForm()
	# Add the form instances to context as key and value
	context = {
		'form': form,
	}
	# Render context to sign-up template
	return render(request, 'app/userauth/sign-up.html', context)
