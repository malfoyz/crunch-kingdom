from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..models import Category


def catalog(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы каталога"""

    search = request.GET.get('search')
    if search:
        categories = Category.objects.filter(name__iregex=search)
    else:
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