# exchangeApp/views.py
from django.db import connection
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from .models import Crypto, Stock, User, CryptoHistory, StocksHistory
from .serializer import CryptoSerializer, StockSerializer, UserSerializer, SignupSerializer, LoginSerializer, CryptoHistorySerializer, StockHistorySerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User as AuthUser
from rest_framework.authtoken.models import Token

class MarketView(APIView):
    def get(self, request):
        cryptos = Crypto.objects.all()
        stocks = Stock.objects.all()
        
        crypto_data = CryptoSerializer(cryptos, many=True).data
        stock_data = StockSerializer(stocks, many=True).data

        return Response({
            'cryptos': crypto_data,
            'stocks': stock_data
        })

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
            user = AuthUser.objects.get(username=serializer.data['username'])
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
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'User or password is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(AuthUser, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'message':"User not found"}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)

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
        limit = request.query_params.get('limit')
        if query:
            try:
                limit = int(limit) if limit else None
            except: 
                return Response({'error': "invalid limit parameter"}, status= status.HTTP_400_BAD_REQUEST)
            results = CryptoHistory.objects.filter(symbol=query)
            if limit is not None:
                results = results[:limit]
            serializer = CryptoHistorySerializer(results,many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'No search term provided'}, status=status.HTTP_400_BAD_REQUEST)

class stockHistoryView(APIView):
    def get(self,request):
        mymodel_objects = StocksHistory.objects.all()
        # Serialize the data
        serializer = StockHistorySerializer(mymodel_objects, many=True)
        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class stockHistoryIdView(RetrieveAPIView):
    queryset = StocksHistory.objects.all()
    serializer_class = StockHistorySerializer

class stockHistorySymbolView(APIView):
    def get(self, request):
        query = request.query_params.get('symbol')
        limit = request.query_params.get('limit')
        if query:
            try:
                limit = int(limit) if limit else None
            except: 
                return Response({'error': "invalid limit parameter"}, status= status.HTTP_400_BAD_REQUEST)
            
            results = StocksHistory.objects.filter(symbol=query)
            if limit is not None:
                results = results[:limit]
            serializer = StockHistorySerializer(results,many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
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

class AverageValuesStockView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            # Get the latest date
            cursor.execute("SELECT MAX(updated_at) FROM api_stockshistory")
            latest_date = cursor.fetchone()[0]
            
            # Fetch the averages for the latest date
            cursor.execute("""
                SELECT 
                    AVG(price) AS average_price, 
                    AVG(volume) AS average_volume, 
                    AVG(coin_market_cap) AS average_market_cap
                FROM api_stockshistory
                WHERE updated_at = %s
            """, [latest_date])
            
            averages = cursor.fetchone()
        
        data = {
            'avgPrice': averages[0],
            'avgVolume': averages[1],
            'avgCoinMarketCap': averages[2]
        }
        
        return Response(data)
    
class AverageValuesCryptoView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            # Get the latest date
            cursor.execute("SELECT MAX(updated_at) FROM api_cryptohistory")
            latest_date = cursor.fetchone()[0]
            
            # Fetch the averages for the latest date
            cursor.execute("""
                SELECT 
                    AVG(price) AS average_price, 
                    AVG(volume) AS average_volume, 
                    AVG(coin_market_cap) AS average_market_cap
                FROM api_cryptohistory
                WHERE updated_at = %s
            """, [latest_date])
            
            averages = cursor.fetchone()
        
        data = {
            'avgPrice': averages[0],
            'avgVolume': averages[1],
            'avgCoinMarketCap': averages[2]
        }
        
        return Response(data)
