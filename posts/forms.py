from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'estado', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Escribe el contenido aquí...'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del autor'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=False, label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False, label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    biografia = forms.CharField(
        required=False,
        label='Biografía',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
    )
    link_web = forms.URLField(
        required=False,
        label='Sitio Web (opcional)',
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
    )
    avatar = forms.ImageField(
        required=False,
        label='Avatar',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['biografia', 'link_web', 'avatar']
        widgets = {
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'link_web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
