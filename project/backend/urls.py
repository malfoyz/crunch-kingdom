from django.urls import path

from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('cart/', cart, name='cart'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:id>/', products_of_category, name='products_of_category'),
    path('', index, name='home'),
]