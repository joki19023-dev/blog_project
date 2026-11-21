from django.contrib import admin
from .models import Perfil, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'autor')
    search_fields = ('titulo', 'contenido')


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'link_web')
    search_fields = ('user__username', 'biografia')


admin.site.register(Post, PostAdmin)
admin.site.register(Perfil, PerfilAdmin)
