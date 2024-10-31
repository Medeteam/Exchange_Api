from django.db import models

class Stock(models.Model):
    symbol = models.CharField(primary_key=True, max_length=10)  # No es necesario `unique=True`, `null=False`, `blank=False`
    web_page = models.URLField(max_length=200)  # Cambiado a URLField para validar correctamente la URL
    started_at = models.DateTimeField(auto_now_add=True)  # Mantiene la fecha solo cuando se crea el objeto

    def __str__(self):
        return f"{self.symbol}"
