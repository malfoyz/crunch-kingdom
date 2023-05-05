from django.shortcuts import render
from .models import Product

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

def main(request):
    products = Product.objects.all()
    new_arrivals = products.order_by('-date_manufacture')[:4] # выборка новинок
    sale_items = products.filter(discount__gt=0).order_by('-discount')[:4] # выборка товаров со скидкой
    context = {
        'products': products,
        'new_arrivals': new_arrivals,
        'sale_items': sale_items
    }
    return render(request, 'backend/main.html', context)
