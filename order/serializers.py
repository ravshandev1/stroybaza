from rest_framework import serializers
from .models import Order, CardItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'card_items', 'promo_code', 'delivery_time', 'created_at', 'address_name', 'house', 'flat',
                  'floor', 'comment']


class CardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = ['product', 'quantity']
