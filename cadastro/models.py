from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Perfil(AbstractUser):

    @property
    def nome(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")
        db_table = "users"


    Preferencias = models.ManyToManyField(
        Preferencias, 
        blank=True, 
        related_name="users",
        verbose_name="Tópicos de Interesse"
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="perfil_set",  
        related_query_name="perfil",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="perfil_set",  
        related_query_name="perfil",
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("Perfil_detail", kwargs={"pk": self.pk})


class Preferencias(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Preferências")

    def __str__(self):
        return self.name