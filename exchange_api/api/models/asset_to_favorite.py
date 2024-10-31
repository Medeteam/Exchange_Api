from django.db import models
from .favorite import Favorites
from .asset import Asset

class AssetsToFavorites(models.Model):
    favorite = models.ForeignKey('Favorites', on_delete=models.CASCADE)
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('favorite', 'asset')

    def __str__(self):
        return f"Asset {self.asset_id} linked to Favorite {self.favorite_id}"
