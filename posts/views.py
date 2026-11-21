from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PerfilForm, PostForm, RegistroUsuarioForm
from .models import Perfil, Post


# LISTAR (Index)
def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, 'posts/lista_posts.html', {'posts': posts})


# DETALLE (Detail)
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


# CREAR (Create) - Protegido con @login_required
@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        initial = {'autor': request.user.get_full_name() or request.user.username}
        form = PostForm(initial=initial)
    return render(request, 'posts/post_form.html', {'form': form, 'accion': 'Crear'})


# EDITAR (Update) - Protegido con @login_required
@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'post': post, 'accion': 'Editar'})


# BORRAR (Delete) - Protegido con @login_required
@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})


# REGISTRO DE USUARIO + CREACIÓN DE PERFIL
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            # El signal post_save crea el Perfil automáticamente; si no existiera, se crea aquí:
            if not Perfil.objects.filter(user=usuario).exists():
                Perfil.objects.create(user=usuario)
            perfil = usuario.perfil
            perfil.biografia = form.cleaned_data.get('biografia', '')
            perfil.link_web = form.cleaned_data.get('link_web', '')
            if form.cleaned_data.get('avatar'):
                perfil.avatar = form.cleaned_data.get('avatar')
            perfil.save()
            login(request, usuario)
            return redirect('lista_posts')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'posts/registro.html', {'form': form})


# VER Y EDITAR PERFIL DE USUARIO
@login_required
def perfil_usuario(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'posts/perfil.html', {'perfil': perfil, 'form': form})


def inicio(request):
    return lista_posts(request)


def acerca(request):
    return render(request, 'posts/acerca.html')
