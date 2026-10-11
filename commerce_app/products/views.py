from django.shortcuts import render
from .models import ChaiVariety
# Create your views here.
def all_products(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'products/all_products.html', {'chais': chais})