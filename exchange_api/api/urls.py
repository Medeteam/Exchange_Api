from django.urls import path, include
from .views import CryptoListCreateView, CryptoDetailView, StockListCreateView, UserListView, SignupView, LoginView, cryptoHistoryView, cryptoHistoryIdView, cryptoHistorySymbolView, StockDetailView, stockHistorySymbolView, stockHistoryIdView, stockHistoryView, MarketView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'api/users', UserListView)

urlpatterns = [
    path ('api/market', MarketView.as_view(), name = 'market-list'),
    path('api/market/crypto/', CryptoListCreateView.as_view(), name='crypto-list-create'),
    path('api/market/crypto/<str:symbol>/', CryptoDetailView.as_view(), name='crypto-detail'),
    path('api/market/stock/', StockListCreateView.as_view(), name='stock-list-create'),
    path('api/market/stock/<str:symbol>/', StockDetailView.as_view(), name='stock-detail'),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/auth/signup/', SignupView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/cryptohistory', cryptoHistoryView.as_view(), name= 'crypto-history'),
    path('api/cryptohistory/<int:pk>/', cryptoHistoryIdView.as_view(), name= 'crypto-history-id'),
    path('api/cryptohistory/symbol/', cryptoHistorySymbolView.as_view(), name= 'crypto-history-symbol'),
    path('api/stockhistory', stockHistoryView.as_view(), name= 'stock-history'),
    path('api/stockhistory/<int:pk>/', stockHistoryIdView.as_view(), name= 'stock-history-id'),
    path('api/stockhistory/symbol/', stockHistorySymbolView.as_view(), name= 'stock-history-symbol')
]
