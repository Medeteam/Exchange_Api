from django.db import models
from .wallet import Wallet
from .asset import Asset

class AssetsToWallet(models.Model):
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('wallet', 'asset')  # Evita duplicados

    def __str__(self):
        return f"Wallet {self.wallet.id} - Asset {self.asset.asset_id}"
