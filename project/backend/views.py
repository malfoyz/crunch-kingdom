from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
)


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

    context = {
        'title': 'Каталог',
    }

    return render(
        request=request,
        template_name='backend/catalog.html',
        context=context,
    )


def products_of_category(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы с постами"""

    context = {
        'title': 'Продукты'
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