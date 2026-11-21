# Blog Project - Gestión de Usuarios, Perfiles (`OneToOneField`), Signals y CRUD Protegido

Aplicación web de Blog construida con **Django** que integra autenticación de usuarios (`django.contrib.auth`), extensión del modelo `User` mediante el modelo `Perfil` (`Profile`) con relación `OneToOneField`, creación automática de perfil mediante señales (`post_save` en `posts/signals.py`) y protección de las rutas de escritura CRUD con `@login_required`.

## Instalación y Cómo Ejecutar las Migraciones

1. Clona el repositorio y crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   ```
2. Instala las dependencias (`Django` y `Pillow`):
   ```bash
   pip install -r requirements.txt
   ```
3. Genera (si hubiera nuevos cambios) y aplica las migraciones para crear la base de datos local `db.sqlite3` con las tablas de usuarios, `Post` y `Perfil`:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Crea un superusuario para acceder al panel `/admin/`:
   ```bash
   python manage.py createsuperuser
   ```
5. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Funcionalidades Implementadas

- **Modelo `Perfil` (`Profile`) en `posts/models.py`**: Relación `OneToOneField(User, on_delete=models.CASCADE)` con los campos `biografia`, `link_web` y `avatar` (`ImageField`).
- **Creación automática de perfil (`posts/signals.py` y `posts/views.py`)**: La señal `post_save` en `posts/signals.py` (conectada desde `posts/apps.py`) crea el perfil automáticamente al registrar un usuario; la vista `registro` completa biografía, sitio web y avatar.
- **Autenticación (`django.contrib.auth`)**: Rutas `/registro/`, `/login/`, `/logout/` y `/perfil/`.
- **Protección de rutas (`@login_required`)**: Al intentar acceder sin sesión a `/post/nuevo/`, `/post/<id>/editar/` o `/post/<id>/eliminar/`, Django redirige automáticamente a `/login/`.
- **Repositorio limpio (`.gitignore`)**: Excluye `db.sqlite3`, archivos temporales `__pycache__`, entornos virtuales y archivos subidos en `/media/`.
