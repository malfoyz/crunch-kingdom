from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
)

from ..models import Product


def index(request: HttpRequest) -> HttpResponse:
    """Обработчик главной страницы"""

    new_products = Product.objects.order_by('-date_manufacture')[:6]
    discount_products = Product.objects.filter(discount__gt=0).order_by('-discount')[:6]

    context = {
        'title': 'Главная',
        'new_products': new_products,
        'discount_products': discount_products,
    }

    return render(
        request=request,
        template_name='backend/main.html',
        context=context,
    )