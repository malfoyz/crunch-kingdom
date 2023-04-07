from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Модель пользователя с доп. данными"""

    # login = models.CharField(
    #     max_length=30,
    #     unique=True,
    #     verbose_name=_('Логин'),
    # )
    # name = models.CharField(
    #     max_length=50,
    #     verbose_name=_('Имя')
    # )

    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Логин',
    )
    phone = models.CharField(
        max_length=11,
        unique=True,
        verbose_name=_('Телефон'),
    )
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        verbose_name=_('Фото'),
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.login} ({self.name})' 
