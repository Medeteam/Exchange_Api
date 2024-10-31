from django.db import models
from .user import User  # Importación de la relación con User

class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True, null=False, unique=True, blank=False)
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=False, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Wallet {self.wallet_id} for User {self.user.username}"