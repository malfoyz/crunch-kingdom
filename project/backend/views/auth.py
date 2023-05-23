from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


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


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """Exit handler"""

    logout(request)
    return redirect('backend:home')
