from django.db import models
from products.models import Product
from accounts.models import Account, phone_regex
from tools.models import Location


class PromoCode(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CardItem(models.Model):
    product = models.ForeignKey(Product, models.SET('Product deleted'), related_name='card_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    @property
    def get_total(self):
        return self.product.price * self.quantity


class Order(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Process'),
        (3, 'Delivered'),
        (4, 'Canceled'),
    )
    user = models.ForeignKey(Account, models.SET('User deleted'), related_name='order')
    status = models.PositiveIntegerField(choices=STATUS, default=1)
    created_at = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=12, validators=[phone_regex])
    card_items = models.ManyToManyField(CardItem)
    promo_code = models.CharField(max_length=250, null=True)
    delivery_time = models.CharField(max_length=255)
    latitude = models.CharField(max_length=30, null=True)
    longitude = models.CharField(max_length=30, null=True)
    address_name = models.CharField(max_length=222, null=True)
    house = models.CharField(max_length=23, null=True)
    flat = models.CharField(max_length=23, null=True)
    floor = models.CharField(max_length=23, null=True)
    comment = models.CharField(max_length=333, null=True)

    def __str__(self):
        return self.user.phone

    @property
    def get_total(self):
        items = self.card_items.all()
        return sum([i.get_total for i in items])

    @property
    def get_count(self):
        items = self.card_items.all()
        return sum([i.quantity for i in items])
