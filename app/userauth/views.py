# app/userauth/views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings

# Define User
User = settings.AUTH_USER_MODEL # get user from this: AUTH_USER_MODEL = 'userauth.User'

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

	# If the user exist, redirect him to the home page
	if request.user.is_authenticated:
		return redirect('core:index')

	# If the use is NOT exist, show him the form and catch its email and password
	if request.method == 'POST':
		emil = request.POST.get('email') # get email from attr name='email' in form input field
		password = request.POST.get('password') # get password from attr name='password' in form input field 

	# Use try block to warn user that something is going wrong
	try:
		user = User.objects.get(email=email) # email (colerd green, is email from db) and emil (colored white, is from the input field)
	except:
		messages.warning(request, f'User with {email} does not exist!')
		return redirect('userauth:login')

	# Check ff user exist
	user = authenticate(request, emil=emil, password=password)
	# If user is known or exist in database
	if user is not None:
		# Log him in directly
		logi(request, user)
		messages.success(request, 'You are logged in!')
		return redirect('core:index')

	# If user is NOT known or DOES NOT exist in database
	else:
		messages.warning(request, 'User does not exist, create an account.')

	return render(request, 'app/userauth/login.html')
