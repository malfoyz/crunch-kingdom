from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

from users.models import CustomUser


class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(
        max_length=50,
        verbose_name=_('Название'),
    )
    description = models.CharField(
        max_length=800,
        blank=True,
        verbose_name=_('Описание'),
    )
    composition = models.CharField(
        max_length=400,
        blank=True,
        verbose_name=_('Состав'),
    )
    discount = models.PositiveSmallIntegerField(
        blank=True,
        verbose_name=_('Скидка'),
        validators=(
            MaxValueValidator(100),
        ),
    )
    quantity = models.PositiveIntegerField(
        blank=True,
        verbose_name=_('Количество'),
    )
    weight = models.PositiveIntegerField(
        blank=True,
        verbose_name=_('Вес'),
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Цена'),
        validators=(
            MinValueValidator(Decimal('0.00')),
        ),
    )
    date_manufacture = models.DateField(
        blank=True,
        verbose_name=_('Дата изготовления'),
    )
    shelf_life = models.CharField(
        blank=True,
        max_length=50,
        verbose_name=_('Срок хранения'),
    )
    photobase = models.OneToOneField(
        to='ProductPhotobase',
        on_delete=models.PROTECT,
        related_name='product',
        related_query_name='product',
        verbose_name=_('Блок фотографий'),
    )
    shop = models.ForeignKey(
        to='Shop',
        on_delete=models.CASCADE,
        related_name='product',
        related_query_name='product',
        verbose_name=_('Магазин'),
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        related_query_name='product',
        verbose_name=_('Категория'),
    )

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    """Модель категории"""

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_('Название'),
    )
    description = models.CharField(
        max_length=800,
        blank=True,
        verbose_name=_('Описание'),
    )
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        verbose_name='Картинка',
    )

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def get_absolute_url(self) -> str:
        return reverse('backend:products_of_category', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.name


class Shop(models.Model):
    """Модель магазина"""

    name = models.CharField(
        max_length=50,
        verbose_name=_('Название')
    )
    description = models.CharField(
        max_length=800,
        blank=True,
        verbose_name=_('Описание'),
    )
    avatar = models.ImageField(
        upload_to='shops/avatars/%Y/%m/%d/',
        verbose_name=_('Аватар'),
    )
    header = models.ImageField(
        upload_to='shops/headers/%Y/%m/%d',
        verbose_name=_('Шапка'),
    )
    owner = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='shops',
        related_query_name='shop',
        verbose_name=_('Владелец'),
    )

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')

    def __str__(self) -> str:
        return self.name


class Deal(models.Model):
    """Модель сделки"""

    quantity = models.PositiveIntegerField(
        verbose_name=_('Количество'),
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Цена/ед.'),
        validators=(
            MinValueValidator(Decimal('0.00')),
        ),
    )
    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата и время'),
    )
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.DO_NOTHING,
        related_name='deals',
        related_query_name='deal',
        verbose_name=_('Покупатель'),
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        related_name='deals',
        related_query_name='deal',
        verbose_name=_('Продукт'),
    )

    class Meta:
        verbose_name = _('Сделка')
        verbose_name_plural = _('Сделки')

    def __str__(self) -> str:
        return str(self.pk)


class Review(models.Model):
    """Абстрактная модель отзыва"""

    mark = models.PositiveSmallIntegerField(
        verbose_name=_('Оценка'),
        validators=(
            MaxValueValidator(5),
        ),
    )
    text = models.CharField(
        max_length=800,
        blank=True,
        verbose_name=_('Текст'),
    )
    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата и время'),
    )

    class Meta:
        abstract = True


class ShopReview(Review):
    """Модель отзыва о магазине"""

    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.DO_NOTHING,
        related_name='shop_reviews',
        related_query_name='shop_review',
        verbose_name=_('Пользователь'),
    )
    shop = models.ForeignKey(
        to='Shop',
        on_delete=models.DO_NOTHING,
        related_name='reviews',
        related_query_name='review',
        verbose_name=_('Магазин'),
    )

    class Meta:
        verbose_name = _('Отзыв о магазине')
        verbose_name_plural = _('Отзывы о магазине')

    def __str__(self) -> str:
        return str(self.mark)


class ProductReview(Review):
    """Модель отзыва о продукте"""

    deal = models.OneToOneField(
        to='Deal',
        on_delete=models.CASCADE,
        related_name='review',
        related_query_name='review',
        verbose_name=_('Сделка'),
    )
    photobase = models.OneToOneField(
        to='ReviewPhotobase',
        on_delete=models.CASCADE,
        blank=True,
        related_name='review',
        related_query_name='review',
        verbose_name=_('Блок фотографий'),
    )

    class Meta:
        verbose_name = _('Отзыв о продукте')
        verbose_name_plural = _('Отзывы о продукте')

    def __str__(self) -> str:
        return str(self.mark)


class Photobase(models.Model):
    """Абстрактная модель блока фотографий"""

    image1 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        verbose_name='Фото 1',
    )
    image2 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 2',
    )
    image3 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 3',
    )
    image4 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 4',
    )
    image5 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 5',
    )
    image6 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 6',
    )
    image7 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 7',
    )
    image8 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 8',
    )
    image9 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 9',
    )
    image10 = models.ImageField(
        upload_to='photobase/%Y/%m/%d',
        blank=True,
        verbose_name='Фото 10',
    )

    class Meta:
        abstract = True


class ReviewPhotobase(Photobase):
    """Модель блока фотографий"""

    class Meta:
        db_table = 'review_photobase'
        verbose_name = 'Блок фотографий отзыва'
        verbose_name_plural = 'Блоки фотографий отзывов'

    def __str__(self) -> str:
        return str(self.pk)


class ProductPhotobase(Photobase):
    """Модель блока фотографий продукта"""

    class Meta:
        db_table = 'product_photobase'
        verbose_name = 'Блок фотографий продукта'
        verbose_name_plural = 'Блоки фотографий продуктов'

    def __str__(self) -> str:
        return str(self.pk)