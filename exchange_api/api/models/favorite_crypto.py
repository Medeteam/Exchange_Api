from django.db import models

class FavoriteCrypto(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    crypto = models.ForeignKey('Crypto', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'crypto')

    def __str__(self):
        return f"Favorite crypto {self.user, self.crypto}"