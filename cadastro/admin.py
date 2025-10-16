from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Perfil
# Register your models here.
@admin.register(Perfil)

class Perfil_Admin(admin.ModelAdmin):
    add_form= CustomUserCreationForm
    form = CustomUserChangeForm
    model= Perfil
    list_display = ("email", "first_name","last_name", "is_active")