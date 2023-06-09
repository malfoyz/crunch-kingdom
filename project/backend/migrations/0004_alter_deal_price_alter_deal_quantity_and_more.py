# Generated by Django 4.2 on 2023-04-08 03:58

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_product_discount_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Цена/ед.'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='mark',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='shopreview',
            name='mark',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
    ]
