from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from ..models import Product, Category


def products(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы товаров"""

    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(name__iregex=search)
        context = {'subtitle': search}
    else:
        products = Product.objects.all()
        context = {'subtitle': 'Все продукты'}

    context = context | {
        'title': 'Продукты',
        'products': products,
    }

    return render(
        request=request,
        template_name='backend/products.html',
        context=context,
    )


def products_of_category(request: HttpRequest, pk: int) -> HttpResponse:
    """Обработчик страницы с постами"""

    products = Product.objects.filter(category__pk=pk)
    category_name = Category.objects.get(pk=pk).name
    context = {
        'title': 'Продукты',
        'products': products,
        'subtitle': category_name,
    }

    return render(
        request=request,
        template_name='backend/products.html',
        context=context,
    )


def product(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы конкретного продукта"""

    product = get_object_or_404(Product, pk=id)
    composition_list = product.composition.lower().split(', ')
    context = {
        'title': f'Продукт {id}',
        'product': product,
        'composition_list': composition_list
    }

    return render(
        request=request,
        template_name='backend/product.html',
        context=context,
    )