# Generated by Django 4.2 on 2023-05-23 06:24

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0006_alter_product_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='deals', related_query_name='deal', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Цена/ед.')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', related_query_name='detail', to='backend.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='deals', related_query_name='deal', to='backend.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Деталь сделка',
                'verbose_name_plural': 'Детали сделки',
            },
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='deal',
        ),
        migrations.DeleteModel(
            name='Deal',
        ),
        migrations.AddField(
            model_name='productreview',
            name='order_detail',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='review', related_query_name='review', to='backend.orderdetail', verbose_name='Деталь сделки'),
            preserve_default=False,
        ),
    ]
