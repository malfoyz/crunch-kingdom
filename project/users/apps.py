from django.apps import AppConfig
from django.contrib.auth.apps import AuthConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


class UsersAuthConfig(AuthConfig):
    verbose_name = _('Группы пользователей')