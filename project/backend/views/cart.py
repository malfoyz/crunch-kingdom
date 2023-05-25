from django.core.mail import send_mail
from django.db.models import F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from ..models import Order, OrderDetail, Product


def cart(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы корзины"""

    cart = request.session.get('cart', {})
    cart_keys = [int(key) for key in cart.keys()]

    products = Product.objects.filter(pk__in=cart_keys).annotate(total_price=F('price')*(100 - F('discount'))/100)
    total_price = 0
    for product in products:
        quantity = cart[str(product.pk)]
        product.total_price *= quantity
        total_price += product.total_price

    context = {
        'title': 'Корзина',
        'products': products,
        'cart': cart,
        'total_price': total_price,
    }

    return render(
        request=request,
        template_name='backend/cart.html',
        context=context,
    )


def payment(request: HttpRequest) -> HttpResponse:
    """Обработчик оплаты заказа"""

    if not request.user.is_authenticated:
        return redirect('backend:register')

    cart = request.session.get('cart', {})
    cart_keys = [int(key) for key in cart.keys()]

    products = Product.objects.filter(pk__in=cart_keys).annotate(total_price=F('price') * (100 - F('discount')) / 100)
    total_price = 0

    order = Order.objects.create(user=request.user)
    email_message = ''

    for product in products:
        quantity = cart[str(product.pk)]
        product.total_price *= quantity
        total_price += product.total_price

        order_detail = OrderDetail.objects.create(
            order=order,
            quantity=cart[str(product.pk)],
            product=product,
            price=product.total_price,
        )

        email_message += f'- {product.name}. Количество: {order_detail.quantity}. Цена: {order_detail.price} руб.\n'

    email_message += f"""\nИтого: {total_price} руб.\n\nДля уточнения деталей заказа и оплаты свяжитесь с менеджером по телефону +7 999 888 77 66.
                     \nЖивите сладко:)"""

    send_mail(
        subject=f'Ваш заказ №{order.pk} оформлен',
        from_email='mufasa133@yandex.ru',
        message=email_message,
        recipient_list=[request.user.email],
    )

    request.session['cart'] = {}
    return redirect('backend:cart')


def add_to_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    """Обработчик добавления товара в корзину"""

    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER'))


def reduce_product_in_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    """Обработчик убавления товара в корзине"""

    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            del cart[str(product_id)]

    request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    """Обработчик удаления товара"""

    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart

    return redirect('backend:cart')


def clear_cart(request: HttpRequest) -> HttpResponse:
    """Обрбаотчик очищения корзины"""

    request.session['cart'] = {}
    return redirect('backend:cart')


