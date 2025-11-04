from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem_id = models.SmallIntegerField()
    rating = models.SmallIntegerField()

    class Meta:
        unique_together = (('user', 'menuitem_id'),)


class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    featured = models.BooleanField(default=False)  # Item of the day / featured

    def __str__(self) -> str:
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart({self.user.username})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = (('cart', 'menuitem'),)

    def line_total(self):
        return self.menuitem.price * self.quantity


class Order(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Preparing'),
        ('O', 'Out for delivery'),
        ('D', 'Delivered'),
        ('C', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order({self.id}) - {self.user.username} - {self.get_status_display()}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def line_total(self):
        return self.unit_price * self.quantity


# ===== signals.py =====
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission


def create_default_groups(sender, **kwargs):
    Group.objects.get_or_create(name='Manager')
    Group.objects.get_or_create(name='Delivery crew')
    Group.objects.get_or_create(name='Customer')


class LittleLemonAPIConfig(AppConfig):
    name = 'littlelemonAPI'

    def ready(self):
        post_migrate.connect(create_default_groups, sender=self)
