from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)

from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):
    """Форма регистрации пользователя"""

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone', 'photo',)

class CustomUserChangeForm(UserChangeForm):
    """Форма изменения пользователя"""

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone', 'photo',)