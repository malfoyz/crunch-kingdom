# Generated by Django 4.2 on 2023-05-20 11:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_category_image_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveSmallIntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Скидка'),
        ),
    ]