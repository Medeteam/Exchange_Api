from django.urls import path
from .views import CryptoListCreateView, CryptoDetailView, StockListCreateView

urlpatterns = [
    path('api/crypto/', CryptoListCreateView.as_view(), name='crypto-list-create'),
    path('api/crypto/<str:symbol>/', CryptoDetailView.as_view(), name='crypto-detail'),
    path('api/stock/', StockListCreateView.as_view(), name='stock-list-create')
]
