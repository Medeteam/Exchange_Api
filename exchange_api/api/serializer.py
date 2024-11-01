from rest_framework import serializers
from .models import Crypto
from .models import Stock
from .models import User

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
        fields = ('user_id', 'name', 'username', 'email', 'password')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()