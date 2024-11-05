# exchangeApp/views.py
from rest_framework import generics, viewsets
from .models import Crypto, Stock, User, CryptoHistory
from .serializer import CryptoSerializer, StockSerializer, UserSerializer, LoginSerializer, CryptoHistorySerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

# Vista para listar y crear registros de Crypto
class CryptoListCreateView(generics.ListCreateAPIView):
    queryset = Crypto.objects.all()  # Recupera todos los registros
    serializer_class = CryptoSerializer  # Usa el serializador de Crypto

# Vista para ver, actualizar y eliminar un registro específico de Crypto
class CryptoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
    lookup_field = 'symbol'  # Utiliza el campo 'symbol' como identificador en la URL

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class  = StockSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # Assuming you have a method to generate a token
                token = "your_token_generation_method(user)"
                return Response({'token': token}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
