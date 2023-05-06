from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
)

from .models import Category, Product


def index(request: HttpRequest) -> HttpResponse:
    """Обработчик главной страницы"""

    context = {
        'title': 'Главная'
    }

    return render(
        request=request,
        template_name='backend/main.html',
        context=context,
    )



def catalog(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы каталога"""

    categories = Category.objects.all()
    context = {
        'title': 'Каталог',
        'categories': categories,
    }

    return render(
        request=request,
        template_name='backend/catalog.html',
        context=context,
    )


def products_of_category(request: HttpRequest, pk: int) -> HttpResponse:
    """Обработчик страницы с постами"""

    products = Product.objects.filter(category__pk=pk)
    context = {
        'title': 'Продукты',
        'products': products,
    }

    return render(
        request=request,
        template_name='backend/products.html',
        context=context,
    )


def cart(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы корзины"""

    context = {
        'title': 'Корзина',
    }
    
    return render(
        request=request,
        template_name='backend/cart.html',
        context=context,
    )


def profile(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы профиля"""

    context = {
        'title': 'Профиль',
    }

    return render(
        request=request,
        template_name='backend/profile.html',
        context=context,
    )