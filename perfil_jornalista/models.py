from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.Charfield(max_lenght=50)
    conteudo = RichTextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    data_atualizada = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-data atualizada"]


