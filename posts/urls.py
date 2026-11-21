from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('inicio/', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    # Rutas CRUD de Posts (protegidas con @login_required para crear, editar y eliminar)
    path('post/nuevo/', views.crear_post, name='crear_post'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),
    # Rutas de Autenticación y Perfil (django.contrib.auth)
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='lista_posts'), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]
