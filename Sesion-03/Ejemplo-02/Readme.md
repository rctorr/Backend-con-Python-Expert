`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 03`](../Readme.md) > Ejemplo-02
## Iniciar la construcción de una aplicación web con Django

### OBJETIVOS
- Conocer como iniciar un proyecto en Django
- Conocer como crear una aplicación
- Conocer y definir una ruta en Django
- Conocer y definir una vista asociada a la ruta

#### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-03/Ejemplo-02`
1. Activar el entorno virtual __Biblioteca__

#### DESARROLLO
1. Crear el proyecto __Biblioteca__ con Django y cambiándonos la carpeta del proyecto:

   ```console
   (Biblioteca) Ejemplo-02 $ django-admin startproject Biblioteca

   (Biblioteca) Ejemplo-02 $ tree Biblioteca
   Biblioteca
   ├── Biblioteca
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── manage.py

   (Biblioteca) Ejemplo-02 $ cd Biblioteca

   (Biblioteca) Ejemplo-02/Biblioteca $
   ```
   ***

1. Crear la aplicación __catalogo__ con el comando:

   ```console
   (Biblioteca) Ejemplo-02/Biblioteca $ python manage.py startapp catalogo

   (Biblioteca) Ejemplo-02/Biblioteca $ tree
   .
   ├── Biblioteca
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── catalogo
   │   ├── admin.py
   │   ├── apps.py
   │   ├── __init__.py
   │   ├── migrations
   │   │   └── __init__.py
   │   ├── models.py
   │   ├── tests.py
   │   └── views.py
   └── manage.py
   ```
   ***

1. Ejecutar el proyecto __Biblioteca__ con:

   ```console
   Ejemplo-02/Biblioteca $ python manage.py runserver
   Watching for file changes with StatReloader
   Performing system checks...

   System check identified no issues (0 silenced).

   You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
   Run 'python manage.py migrate' to apply them.

   June 19, 2019 - 10:38:22
   Django version 2.2.2, using settings 'Biblioteca.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.   
   ```
   Si se abre la url indicada, se observará lo mismo que el "hola mundo!", así que sigamos un poco más adelante, nuestro objetivo es mostrar la página `index.html` pero como parte de la aplicación web.

   __Nota:__ Como el servidor bloque la terminal, vamos a dejar esta terminal aquí y para los siguiente comandos abrir otra terminal, activar el entorno virtual Biblioteca y cambiarse a la carpeta de trabajo `Sesion-03/Ejemplo-02/Biblioteca/`.

1. Agrega la aplicación __catalogo__ a la configuración en el archivo `Biblioteca/Biblioteca/settings.py`:

   ```python
   # Application definition

   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'catalogo',
   ]   
   ```

   __Revisar el flujo de una petición HTTP para el caso de Django:__

   [Ver diapos]

1. Mapear la url `/` con las rutas generales del proyecto __Biblioteca__ hacia las rutas de la aplicación __catalogo__

   ```
   url / -> Biblioteca/Biblioteca/urls.py -> Biblioteca/catalogo/urls.py
   ```

   __En el archivo `Biblioteca/Biblioteca/urls.py` agregar lo siguiente:__

   ```python
   from django.contrib import admin
   from django.urls import path, include  # modificada

   urlpatterns = [
       path('', include("catalogo.urls")),  # agregada
       path('admin/', admin.site.urls),
   ]
   ```

   En la vetana donde se está ejecutando el proyecto __Biblioteca__ se puede observar el siguiente mensaje de error:

   ```console
   (Biblioteca) Ejemplo-02/Biblioteca $ python manage.py runserver
   [...]
   File "<frozen importlib._bootstrap>", line 965, in _find_and_load_unlocked
   ModuleNotFoundError: No module named 'catalogo.urls'
   ```
   Lo que indica que nos falta crear el archivo `urls.py` dentro de la carpeta `Biblioteca/catalogo/`

1. Mapear la url `/` con las rutas de la aplicación __catalogo__

   ```
   url / -> Biblioteca/catalogo/urls.py -> Biblioteca/catalogo/views.py
   ```

   __Crear el archivo `Biblioteca/catalogo/urls.py` con el siguiente contenido:__

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```

   __Reiniciar Django para observar el resultado:__

   ```console
   [...]
   File "/home/rctorr/repos/Curso-Python-Expert/Sesion-03/Ejemplo-02/Biblioteca/catalogo/urls.py", line 5, in <module>
     path('', views.index, name='index'),
   AttributeError: module 'catalogo.views' has no attribute 'index'
   ```
   Lo que indica que en el archivo `catalogo/views.py` no existe una función llamada `index`, así que toca agregar dicha función.

1. Agregar la función/vista `index` al archivo `Biblioteca/catalogo/views.py` con el siguiente contenido:

   ```python
   from django.http import HttpResponse
   from django.shortcuts import render

   # Create your views here.
   def index(request):
       """ Vista para atender la petición de la url / """
       return HttpResponse("<h2>Soy la página de inicio! Soy el amor te tu vida!</h2>")
   ```

   __Nota: Si la aplicación Django no está iniciada, iniciarla en este momento y abrir la siguiente url en el navegador__

   http://127.0.0.1:8000

   __El resultado debería ser el siguiente:__

   ![Página de inicio Biblioteca](assets/biblioteca-index-01.png)
   ***
