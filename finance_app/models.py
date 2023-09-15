from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.TextField(max_length=150)
    last_name = models.TextField(max_length=150)
    email = models.TextField(null=False, max_length=255)
    current_balance = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField(auto_now_add=True, null=False)


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField(auto_now_add=True, null=False)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    volume = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField(auto_now_add=True, null=False)
