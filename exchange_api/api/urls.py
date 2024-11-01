from django.urls import path, include
from .views import CryptoListCreateView, CryptoDetailView, StockListCreateView, UserListView, UserCreateView, LoginView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'api/users', UserListView)

urlpatterns = [
    path('api/crypto/', CryptoListCreateView.as_view(), name='crypto-list-create'),
    path('api/crypto/<str:symbol>/', CryptoDetailView.as_view(), name='crypto-detail'),
    path('api/stock/', StockListCreateView.as_view(), name='stock-list-create'),
    # path('', include(router.urls)),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/auth/signup', UserCreateView.as_view(), name='signup'),
    path('api/auth/login', LoginView.as_view(), name='login'),
]
