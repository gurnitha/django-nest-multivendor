# app/userauth/views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect

# Locals
from app.userauth.forms import UserRegisterForm

# Register View
def register_view(request):

	if request.method == 'POST':
		# Use the UserRegisterForm
		form = UserRegisterForm(request.POST or NONE)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Hey {username}, your account was created successfully!')
			new_user = authenticate(
				username=form.cleaned_data['email'],
				password=form.cleaned_data['password1'])
			login(request, new_user)
			return redirect('userauth:login')

	else: 
		form = UserRegisterForm()

	# Add the form instances to context as key and value
	context = {
		'form': form,
	}

	# Render context to sign-up template
	return render(request, 'app/userauth/register.html', context)


# Login View
def login_view(request):
	return render(request, 'app/userauth/login.html')
