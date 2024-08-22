from typing import List, Dict, Any, Union

from django.contrib.auth.models import User

from .models import Product


class CartService:

    @staticmethod
    def calculate_cart_total(cart: Dict[str, int], products: List[Dict[str, Any]]) -> float:
        total_price = 0

        for product in products:
            quantity = cart.get(str(product['pk']), 0)
            total_price += product['total_price'] * quantity

        return total_price

    @staticmethod
    def create_order(user, products, cart) -> Dict[str, Union[User, List[Dict[str, Union[int, Product]]], float]]:
        order_details = []
        total_price = 0

        for product in products:
            quantity = cart.get(str(product['pk']), 0)
            product_total_price = product['total_price'] * quantity
            total_price += product_total_price

            order_details.append({
                'quantity': quantity,
                'product': product,
                'price': product_total_price,
            })

        return {
            'user': user,
            'order_details': order_details,
            'total_price': total_price,
        }

    @staticmethod
    def generate_email_message(order: Dict[str, Union[User, List[Dict[str, Union[int, Product]]], float]]) -> str:
        email_message = ''

        for order_detail in order['order_details']:
            product = order_detail['product']
            email_message += f'- {product["name"]}. Количество: {order_detail["quantity"]}. Цена: {order_detail["price"]} руб.\n'

        email_message += f"""\nИтого: {order['total_price']} руб.\n\nДля уточнения деталей заказа и оплаты свяжитесь с менеджером по телефону +7 999 888 77 66.
                         \nЖивите сладко:)"""

        return email_message

    @staticmethod
    def send_order_confirmation_email(order: Dict[str, Union[User, List[Dict[str, Union[int, Product]]], float]], user_email: str):
        email_message = CartService.generate_email_message(order)

        # send_mail(
        #     subject=f'Ваш заказ №{order.pk} оформлен',
        #     from_email='mufasa133@yandex.ru',
        #     message=email_message,
        #     recipient_list=[user_email],
        # )

        # Для целей тестирования заменим на print
        print("Email message:", email_message)

    @staticmethod
    def clear_cart(session: Dict[str, Any]):
        session['cart'] = {}
