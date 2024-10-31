from django.db import models
from .crypto import Crypto  # Importación directa del modelo Crypto

class CryptoHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    symbol = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    coin_market_cap = models.BigIntegerField(null=False)
    volume = models.BigIntegerField(null=False)

    def __str__(self):
        return f"History {self.history_id} for {self.symbol.symbol} at {self.updated_at}"
