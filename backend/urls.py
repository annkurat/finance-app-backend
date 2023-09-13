from django.contrib import admin
from finance_app.views import UserCreateView, StockCreateView, TransactionCreateView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UserCreateView.as_view(), name='user-create'),
    path('api/stock/', StockCreateView.as_view(), name='stock-create'),
    path('api/transaction/', TransactionCreateView.as_view(),
         name='transaction-create'),
]
