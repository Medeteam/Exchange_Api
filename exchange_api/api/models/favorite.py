from django.db import models

class Favorites(models.Model):
    favorite_id = models.AutoField(primary_key=True, null=False, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favorite {self.favorite_id}"
    