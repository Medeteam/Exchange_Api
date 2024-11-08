from django.urls import path, include
from .views import CryptoListCreateView, CryptoDetailView, StockListCreateView,UserListView, SignupView, LoginView, cryptoHistoryView, cryptoHistoryIdView, cryptoHistorySymbolView, StockDetailView, stockHistorySymbolView, stockHistoryIdView, stockHistoryView, MarketView
from .views import HighestPriceStockView, HighestPriceCryptoView, LowestPriceStockView, LowestPriceCryptoView, AverageValuesStockView, AverageValuesCryptoView, FavoriteCryptoView, FavoriteStockView, FavoritesView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/market/', MarketView.as_view(), name = 'market-list'),
    path('api/market/cryptos/', CryptoListCreateView.as_view(), name='crypto-list-create'),
    path('api/market/cryptos/<str:symbol>/', CryptoDetailView.as_view(), name='crypto-detail'),
    path('api/market/stocks/', StockListCreateView.as_view(), name='stock-list-create'),
    path('api/market/stocks/<str:symbol>/', StockDetailView.as_view(), name='stock-detail'),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/auth/signup/', SignupView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/market/cryptohistory/', cryptoHistoryView.as_view(), name= 'crypto-history'),
    path('api/market/cryptohistory/<int:pk>/', cryptoHistoryIdView.as_view(), name= 'crypto-history-id'),
    path('api/market/cryptohistory/symbol/', cryptoHistorySymbolView.as_view(), name= 'crypto-history-symbol'),
    path('api/market/stockhistory', stockHistoryView.as_view(), name= 'stock-history'),
    path('api/market/stockhistory/<int:pk>/', stockHistoryIdView.as_view(), name= 'stock-history-id'),
    path('api/market/stockhistory/symbol/', stockHistorySymbolView.as_view(), name= 'stock-history-symbol'),
    path('api/market/cryptohistory/symbol/', cryptoHistorySymbolView.as_view(), name= 'crypto-history-symbol'),
    path('api/market/stocks/highest-price/', HighestPriceStockView.as_view(), name='highest-stock-price'),
    path('api/market/cryptos/highest-price/', HighestPriceCryptoView.as_view(), name='highest-crypto-price'),
    path('api/market/stocks/lowest-price/', LowestPriceStockView.as_view(), name='lowest-stock-price'),
    path('api/market/cryptos/lowest-price/', LowestPriceCryptoView.as_view(), name='lowest-crypto-price'),
    path('api/market/stocks/average/', AverageValuesStockView.as_view(), name='average-stock-values'),
    path('api/market/cryptos/average/', AverageValuesCryptoView.as_view(), name='average-crypto-values'),
    path('api/users/favorites/', FavoritesView.as_view(), name='favorites'),
    path('api/users/favorites/cryptos/', FavoriteCryptoView.as_view(), name='favorite-cryptos'),
    path('api/users/favorites/stocks/', FavoriteStockView.as_view(), name='favorite-stocks'),
]
