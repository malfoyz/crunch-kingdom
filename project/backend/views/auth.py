from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def register(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы регистрации"""

    context = {
        'title': 'Регистрация',
    }

    return render(
        request=request,
        template_name='backend/register.html',
        context=context,
    )