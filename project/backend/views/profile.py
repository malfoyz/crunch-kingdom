from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def profile(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы профиля"""

    context = {
        'title': 'Профиль',
    }

    if request.user.is_authenticated:
        template_name = 'backend/profile.html'
    else:
        template_name = 'backend/profile_unregistered.html'

    return render(
        request=request,
        template_name=template_name,
        context=context,
    )