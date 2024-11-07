# exchangeApp/views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from .models import Crypto, Stock, User, CryptoHistory, StocksHistory
from .serializer import CryptoSerializer, StockHistorySerializer, StockSerializer, UserSerializer, SignupSerializer, CryptoHistorySerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User as AuthUser
from rest_framework.authtoken.models import Token


class CryptoListCreateView(generics.ListCreateAPIView):
    queryset = Crypto.objects.all() 
    serializer_class = CryptoSerializer  

class CryptoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
    lookup_field = 'symbol'  

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class  = StockSerializer

class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'symbol'

class UserListView(generics.ListAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer

# With rest framework model
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = AuthUser.objects.get(username=request.data['username'], email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()

            api_user = User.objects.create(
                username=request.data['username'],
                email=request.data['email'],
                password=user.password
            )
            api_user.save()

            token = Token.objects.create(user=user)
            return Response({
                'message': 'User created successfully',
                'userId': user.id,
                'username': user.username,
                'token': token.key,
            })
        return Response(serializer.errors, status=status.HTTP_200_OK)


# With own model
# class SignupView(APIView):
#     def post(self, request):
#         serializer = SignupSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token = Token.objects.create(user=user)
#             return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(AuthUser, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'message':"User not found"}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username})

class cryptoHistoryView(APIView):
    def get(self,request):
        mymodel_objects = CryptoHistory.objects.all()
        # Serialize the data
        serializer = CryptoHistorySerializer(mymodel_objects, many=True)
        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class cryptoHistoryIdView(RetrieveAPIView):
    queryset = CryptoHistory.objects.all()
    serializer_class = CryptoHistorySerializer

class cryptoHistorySymbolView(APIView):
    def get(self, request):
        query = request.query_params.get('symbol')
        if query:
            results = CryptoHistory.objects.filter(symbol=query)
            serializer = CryptoHistorySerializer(results,many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'No search term provided'}, status=status.HTTP_400_BAD_REQUEST)

class HighestPriceStockView(APIView):
    def get(self, request):
        highest_price_stock = StocksHistory.objects.order_by('-updated_at', '-price').first()
        serializer = StockHistorySerializer(highest_price_stock)
        return Response(serializer.data)
    
class HighestPriceCryptoView(APIView):
    def get(self, request):
        highest_price_crypto = CryptoHistory.objects.order_by('-updated_at', '-price').first()
        serializer = CryptoHistorySerializer(highest_price_crypto)
        return Response(serializer.data)

class LowestPriceStockView(APIView):
    def get(self, request):
        lowest_price_stock = StocksHistory.objects.order_by('-updated_at', 'price').first()
        serializer = StockHistorySerializer(lowest_price_stock)
        return Response(serializer.data)
    
class LowestPriceCryptoView(APIView):
    def get(self, request):
        lowest_price_crypto = CryptoHistory.objects.order_by('-updated_at', 'price').first()
        serializer = CryptoHistorySerializer(lowest_price_crypto)
        return Response(serializer.data)
