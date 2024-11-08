from rest_framework import serializers
from .models import Crypto
from .models import Stock
from .models import CryptoHistory
from .models import StocksHistory
from .models import FavoriteCrypto, FavoriteStock
from django.contrib.auth.models import User

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class CryptoHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoHistory
        fields = '__all__'

class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StocksHistory
        fields = '__all__'

class FavoriteCryptoSerializer(serializers.ModelSerializer):
    crypto = CryptoSerializer()

    class Meta:
        model = FavoriteCrypto
        fields = ['crypto']

class FavoriteStockSerializer(serializers.ModelSerializer):
    stock = StockSerializer()

    class Meta:
        model = FavoriteStock
        fields = ['stock']

class MarketCryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoHistory
        fields = ('symbol_id' , 'price', 'volume', 'coin_market_cap')

class MarketStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StocksHistory
        fields = ('symbol_id' , 'price', 'volume', 'coin_market_cap')