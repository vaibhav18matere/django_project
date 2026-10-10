from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, 'website/index.html')

def About(request):
    return HttpResponse("About Page")

def Contact(request):
    return HttpResponse("Contact Page")

def Services(request):
    return HttpResponse("Services Page")

def Products(request):
    return HttpResponse("Products Page")