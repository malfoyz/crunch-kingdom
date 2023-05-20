from django.urls import path

from .views.auth import register
from .views.cart import (
    add_to_cart, cart, clear_cart,
    reduce_product_in_cart, remove_from_cart,
)
from .views.catalog import catalog
from .views.index import index
from .views.orders import orders
from .views.products import (
    product, products, products_of_category,
)
from .views.profile import profile


app_name = 'backend'
urlpatterns = [
    path('register/', register, name='register'),
    path('orders/', orders, name='orders'),
    path('profile/', profile, name='profile'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('cart/remove/<int:product_id>/',
         remove_from_cart, name='remove_from_cart'),
    path('cart/reduce/<int:product_id>/',
         reduce_product_in_cart, name='reduce_product_in_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('catalog/<int:pk>/',
         products_of_category, name='products_of_category'),
    path('catalog/', catalog, name='catalog'),
    path('products/<int:id>/', product, name='product'),
    path('products/', products, name='products'),
    path('', index, name='home'),
]