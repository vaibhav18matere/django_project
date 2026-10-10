from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, 'website/index.html')

def About(request):
    return render(request, 'website/about.html')

def Contact(request):
    return render(request, 'website/contact.html')

def Services(request):
    return render(request, 'website/services.html')

def Products(request):
    return render(request, 'website/products.html')