from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    titulo = models.Charfield(max_lenght=50)
    conteudo = RichTextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    data_atualizada = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-data atualizada"]