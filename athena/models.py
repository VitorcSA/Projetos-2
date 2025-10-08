from django.db import models
from django.contrib.auth.models import User 
from django.contrib.gis.geos import Point
# Create your models here.
class Perfil(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    def __str__(self):
       return f"Perfil de {self.user.username}"
    
class Localização(models.Model):
    session_id = models.CharField(max_length=40, unique=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    location = models.PointField(null=True, blank=True, srid=4326)
    city = models.CharField(max_length=100, blank=True)
    user_agent = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save_location(self, latitude, longitude, session_id, ip_address=None, user_agent=None):
        self.session_id = session_id
        self.ip_address = ip_address
        self.user_agent = user_agent or ''
        self.location = Point(longitude, latitude, srid=4326)
        self.save()
    def __str__(self):
        return f"Localização anônima: {self.session_id[:8]}..."
