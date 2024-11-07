from django.db import models

class FavoriteStock(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'stock')

    def __str__(self):
        return f"Favorite stock {self.user, self.stock}"