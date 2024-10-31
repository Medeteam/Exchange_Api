from django.db import models
from .crypto import Crypto
from .stock import Stock

class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True, null=False, unique=True, blank=False)
    crypto_symbol = models.ForeignKey('Crypto',on_delete=models.CASCADE)
    stock_symbol = models.ForeignKey('Stock',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Asset {self.asset_id} - {self.crypto_symbol or self.stock_symbol}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                    models.Q(crypto_symbol__isnull=False) | models.Q(stock_symbol__isnull=False)
                ),
                name='at_least_one_symbol_must_be_present'
            )
        ]