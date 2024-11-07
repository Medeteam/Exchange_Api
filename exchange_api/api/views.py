# exchangeApp/views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from .models import Crypto, Stock, User, CryptoHistory, StocksHistory
from .serializer import CryptoSerializer, StockSerializer, UserSerializer, SignupSerializer, CryptoHistorySerializer, StockHistorySerializer
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
