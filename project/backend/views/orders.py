from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..models import Order, Product


def orders(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы истории заказов"""

    orders = Order.objects.filter(user=request.user)
    context = {
        'title': 'История заказов',
        'orders': orders,
    }

    return render(
        request=request,
        template_name='backend/orders.html',
        context=context,
    )