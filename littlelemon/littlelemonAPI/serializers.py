from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import (MenuItem, Category, Rating, Cart, CartItem, Order, OrderItem)
from django.db import transaction


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # add to Customer group
        customer_group, _ = Group.objects.get_or_create(name='Customer')
        user.groups.add(customer_group)
        # create cart
        Cart.objects.create(user=user)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'category', 'category_id', 'featured']

    def validate_price(self, value):
        if value < 5:
            raise serializers.ValidationError('Price must be at least 5')
        return value


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Rating
        fields = ['user', 'menuitem_id', 'rating']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields=['user', 'menuitem_id']
            )
        ]
        extra_kwargs = {
            'rating': {'min_value': 0, 'max_value': 5},
        }


class CartItemSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'menuitem', 'menuitem_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
        read_only_fields = ['user']


class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'menuitem', 'menuitem_id', 'quantity', 'unit_price']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'order_items', 'created_at']
        read_only_fields = ['user', 'total', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('order_items')
        user = self.context['request'].user
        with transaction.atomic():
            order = Order.objects.create(user=user, **validated_data)
            total = 0
            for item in items_data:
                menuitem = MenuItem.objects.get(pk=item['menuitem_id'])
                oi = OrderItem.objects.create(
                    order=order,
                    menuitem=menuitem,
                    quantity=item['quantity'],
                    unit_price=menuitem.price
                )
                total += oi.line_total()
            order.total = total
            order.save()
        return order
