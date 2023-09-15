from rest_framework import serializers
from .models import User, Stock, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    stock = StockSerializer(source='stock_id', read_only=True)
    class Meta:
        model = Transaction
        fields = ('id', 'user_id', 'stock_id', 'volume', 'purchase_price', 'created_at', 'stock')

