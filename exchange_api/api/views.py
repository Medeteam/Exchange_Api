# exchangeApp/views.py
from rest_framework import generics
from .models import Crypto
from .models import Stock
from .serializer import CryptoSerializer
from .serializer import StockSerializer

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