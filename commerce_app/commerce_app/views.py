from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello, World!")

def About(request):
    return HttpResponse("About Page")

def Contact(request):
    return HttpResponse("Contact Page")

def Services(request):
    return HttpResponse("Services Page")

def Products(request):
    return HttpResponse("Products Page")