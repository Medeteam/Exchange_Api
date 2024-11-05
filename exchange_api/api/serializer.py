from rest_framework import serializers
from .models import Crypto
from .models import Stock
from .models import CryptoHistory
# from .models import User
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password

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

# Own class model
# class SignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         user = User.objects.create(**validated_data)
#         return user

class CryptoHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoHistory
        fields = '__all__'