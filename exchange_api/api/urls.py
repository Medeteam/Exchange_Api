from django.urls import path, include
from .views import CryptoListCreateView, CryptoDetailView, StockListCreateView,UserListView, SignupView, LoginView, cryptoHistoryView, cryptoHistoryIdView, cryptoHistorySymbolView, StockDetailView
from .views import HighestPriceStockView, HighestPriceCryptoView, LowestPriceStockView, LowestPriceCryptoView, AverageValuesStockView, AverageValuesCryptoView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'api/users', UserListView)

urlpatterns = [
    path('api/crypto/', CryptoListCreateView.as_view(), name='crypto-list-create'),
    path('api/crypto/<str:symbol>/', CryptoDetailView.as_view(), name='crypto-detail'),
    path('api/stock/', StockListCreateView.as_view(), name='stock-list-create'),
    path('api/stock/<str:symbol>/', StockDetailView.as_view(), name='stock-detail'),
    # path('', include(router.urls)),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/auth/signup/', SignupView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/cryptohistory/', cryptoHistoryView.as_view(), name= 'crypto-history'),
    path('api/cryptohistory/<int:pk>/', cryptoHistoryIdView.as_view(), name= 'crypto-history-id'),
    path('api/cryptohistory/symbol/', cryptoHistorySymbolView.as_view(), name= 'crypto-history-symbol'),
    path('api/market/stocks/highest-price/', HighestPriceStockView.as_view(), name='highest-stock-price'),
    path('api/market/cryptos/highest-price/', HighestPriceCryptoView.as_view(), name='highest-crypto-price'),
    path('api/market/stocks/lowest-price/', LowestPriceStockView.as_view(), name='lowest-stock-price'),
    path('api/market/cryptos/lowest-price/', LowestPriceCryptoView.as_view(), name='lowest-crypto-price'),
    path('api/market/stocks/average', AverageValuesStockView.as_view(), name='average-stock-values'),
    path('api/market/cryptos/average', AverageValuesCryptoView.as_view(), name='average-crypto-values')
]
