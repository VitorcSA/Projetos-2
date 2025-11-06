from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Perfil

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields=(
            "username",
            "email"
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta: 
        model = Perfil
        fields= "__all__"