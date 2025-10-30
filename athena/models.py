from django.db import models
from django.contrib.auth.models import User 

class Tag(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome}"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")

    tags = models.ManyToManyField(Tag, related_name="tags");    

    def __str__(self):
       return f"Perfil de {self.user.username}"

