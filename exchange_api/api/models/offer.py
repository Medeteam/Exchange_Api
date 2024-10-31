from django.db import models
from .wallet import Wallet

class Offers(models.Model):
    offer_id = models.AutoField(primary_key=True, null=False, unique=True, blank=False)
    publisherWallet = models.ForeignKey("Wallet", on_delete=models.SET_NULL, null=True, blank=True)
    OFFER_TYPES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]
    order_type = models.CharField(max_length=4, choices=OFFER_TYPES, default='buy')
    price = models.DecimalField(max_digits=10,decimal_places=4)
    
    def __str__(self):
        return f"Offer {self.offer_id}: {self.get_order_type_display()} at {self.price}"