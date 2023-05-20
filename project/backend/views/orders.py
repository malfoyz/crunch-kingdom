from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..models import Product


def orders(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы истории заказов"""

    products = Product.objects.filter(pk__in=[1, 2])
    context = {
        'title': 'История заказов',
        'products': products,
    }

    return render(
        request=request,
        template_name='backend/orders.html',
        context=context,
    )