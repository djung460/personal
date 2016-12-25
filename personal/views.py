from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'personal/home.html')

def blog(request):
	return render(request, 'personal/blog.html')
