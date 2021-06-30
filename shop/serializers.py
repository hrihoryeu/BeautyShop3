from rest_framework import serializers
from shop.models import Product
from orders.models import Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'product_type', 'brand']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'created', 'updated', 'paid']
