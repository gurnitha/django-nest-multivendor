# app/userauth/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.userauth.forms import UserRegisterForm

# Register View
def register_view(request):

	if request.method == 'POST':
		# Use the UserRegisterForm
		form = UserRegisterForm(request.POST or NONE)
		if form.is_valid():
			form.save()

	else: 
		form = UserRegisterForm()

	# Add the form instances to context as key and value
	context = {
		'form': form,
	}

	# Render context to sign-up template
	return render(request, 'app/userauth/sign-up.html', context)
