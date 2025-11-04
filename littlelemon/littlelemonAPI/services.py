from django.shortcuts import get_object_or_404
from .models import Cart, CartItem, MenuItem, Order, OrderItem
from django.db import transaction


class CartService:
    @staticmethod
    def get_or_create_cart_for_user(user):
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart

    @staticmethod
    def add_item(cart, menuitem_id, quantity=1):
        menuitem = get_object_or_404(MenuItem, pk=menuitem_id)
        ci, created = CartItem.objects.get_or_create(cart=cart, menuitem=menuitem, defaults={'quantity': quantity})
        if not created:
            ci.quantity += quantity
            ci.save()
        return ci

    @staticmethod
    def clear_cart(cart):
        cart.items.all().delete()

    @staticmethod
    def create_order_from_cart(cart):
        with transaction.atomic():
            order = Order.objects.create(user=cart.user)
            total = 0
            for ci in cart.items.select_related('menuitem'):
                OrderItem.objects.create(order=order, menuitem=ci.menuitem, quantity=ci.quantity, unit_price=ci.menuitem.price)
                total += ci.line_total()
            order.total = total
            order.save()
            cart.items.all().delete()
            return order