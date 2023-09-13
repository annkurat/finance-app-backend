from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, StockSerializer, TransactionSerializer
from .models import User, Stock, Transaction
# Create your views here.


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StockCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class TransactionCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
