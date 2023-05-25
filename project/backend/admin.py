from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from .models import *
from .forms import (
    ProductForm,
    ProductReviewForm,
    ShopReviewForm,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Редактор модели продукта"""

    form = ProductForm


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    """Редактор модели отзыва о продукте"""

    form = ProductReviewForm


@admin.register(ShopReview)
class ShopReviewAdmin(admin.ModelAdmin):
    """Редактор модели отзыва о магазине"""

    form = ShopReviewForm


admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(ProductPhotobase)
admin.site.register(ReviewPhotobase)

