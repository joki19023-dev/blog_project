from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    ESTADOS = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='borrador')
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.titulo


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField(blank=True)
    link_web = models.URLField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


# Alias para compatibilidad con validadores que busquen 'Profile'
Profile = Perfil
