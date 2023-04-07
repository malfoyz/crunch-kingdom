from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    CustomUserCreationFrom,
    CustomUserChangeForm,
)
from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Редактор модели пользователя"""

    add_form = CustomUserCreationFrom
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username',)
    list_filter = ('email', 'username',)

    add_fieldsets = (
        #*UserAdmin.add_fieldsets,
        (None, {
            'fields' : ('username', 'email', 'first_name', 'last_name', 'phone', 'photo', 'password1', 'password2',)
        }),
    )

    fieldsets = (
        #*UserAdmin.fieldsets,
        (None, {
            'fields': ('username', 'email', 'first_name', 'last_name', 'phone', 'photo')
        }),
    )

    

