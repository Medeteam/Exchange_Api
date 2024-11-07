from django.db import models

# Modelo para la tabla 'Users'
class User(models.Model):
    user_id = models.AutoField(primary_key=True, null=False, unique=True, blank=False)
    name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username