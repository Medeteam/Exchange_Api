from django.db import models
from .offer import Offers  # Asegúrate de que el archivo se llama offer.py y el modelo es Offer
from .wallet import Wallet  # Asumo que tienes un modelo Wallet

class TransactionHistory(models.Model):
    transaction_id = models.AutoField(primary_key=True, null=False, unique=True, blank=False)
    offer = models.ForeignKey('Offers', on_delete=models.CASCADE, related_name='transaction_histories')
    price = models.DecimalField(max_digits=10, decimal_places=4)
    wallet_client = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='client_transactions')
    wallet_publisher = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='publisher_transactions')

    def __str__(self):
        return f"Transaction {self.transaction_id} for offer {self.offer_id} at price {self.price}"
