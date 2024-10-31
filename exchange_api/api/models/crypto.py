from django.db import models

class Crypto(models.Model):
    symbol = models.CharField(primary_key=True, max_length=10)  
    web_page = models.URLField(max_length=200)  
    start_date = models.DateTimeField()  

    def __str__(self):
        return f"{self.symbol}"
