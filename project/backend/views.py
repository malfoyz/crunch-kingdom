from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
)


def index(request: HttpRequest) -> HttpResponse:
    """Обработчик главной страницы"""

    return render(
        request=request,
        template_name='backend/main.html',
    )



def catalog(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы каталога"""

    return render(
        request=request,
        template_name='backend/catalog.html',
    )


def products_of_category(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы с постами"""

    return render(
        request=request,
        template_name='backend/products.html',
    )


def cart(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы корзины"""
    
    return render(
        request=request,
        template_name='backend/cart.html',
    )


def profile(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы профиля"""

    return render(
        request=request,
        template_name='backend/profile.html',
    )