# app/core/views.py

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'app/core/index.html')
