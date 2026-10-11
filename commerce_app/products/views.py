from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404
def all_products(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'products/all_products.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'products/chai_details.html', {'chai': chai})