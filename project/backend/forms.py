from django import forms
from django.forms import widgets

from .models import (
    Product,
    ProductReview,
    ShopReview,
)


class ProductForm(forms.ModelForm):
    """Форма связанная с моделью продукта"""

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'discount': widgets.NumberInput(attrs={'min': 0, 'max': 100}),
        }


class ProductReviewForm(forms.ModelForm):
    """Форма связанная с моделью отзыва о продукте"""

    class Meta:
        model = ProductReview
        fields = '__all__'
        widgets = {
            'mark': widgets.NumberInput(attrs={'min': 0, 'max': 5}),
        }


class ShopReviewForm(forms.ModelForm):
    """Форма связанная с моделью отзыва о магазине"""

    class Meta:
        model = ShopReview
        fields = '__all__'
        widgets = {
            'mark': widgets.NumberInput(attrs={'min': 0, 'max': 5}),
        }