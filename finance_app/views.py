from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, StockSerializer, TransactionSerializer
from .models import User, Stock, Transaction
# Create your views here.


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        email = self.request.query_params.get('email')
        if email:
            queryset = queryset.filter(email=email)
        return queryset


class StockCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class TransactionCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            return Transaction.objects.filter(user_id=user_id)
        return Transaction.objects.all()
