`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 10`](../Readme.md) > Ejemplo-01
## Definiendo y agregando autenticación de entrada usando el modelo User de Django

### OBJETIVO
- Conocer el modelo User de Django
- Crear autenticación de entrada para una página de la aplicación

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Clase-10/Ejemplo-01`
1. Diagrama del modelo entidad-relación para el proyect __Biblioteca__

   ![Modelo entidad-relación para Biblioteca](modelo-entidad-relacion.jpg)


### DESARROLLO
1. Conociendo el modelo User de Django:

   __Iniciar el shell de Django:__
   ```console
   Ejemplo-01/Biblioteca $ python manage.py shell
   Python 3.7.3 (default, Mar 27 2019, 22:11:17)
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   (InteractiveConsole)
   >>>
   ```

   __Listando los registros en el modelo User:__

   ```python
   >>> from django.contrib.auth.models import User
   >>> User.objects.all()
   <QuerySet [<User: biblioteca>]>
   >>> u1 = User.objects.get(pk=1)
   >>> u1.username
   'biblioteca'
   >>> u1.email
   'biblioteca@gmail.com'
   ```

   __Validando datos de usuario contra los datos del modelo User:__

   ```python
   >>> from django.contrib.auth import authenticate
   >>> username = "biblioteca"
   >>> password = "biblio"
   >>> authenticate(username=username, password=password)
   >>> acceso = authenticate(username=username, password=password)
   >>> print(acceso)
   None
   >>> acceso == None
   True
   >>> password = "biblioteca"
   >>> acceso = authenticate(username=username, password=password)
   >>> acceso
   <User: biblioteca>
   ```

1. Modificando la vista `login()` para incluir la validación usando el modelo User de Django.

   __Modificando los import para poder utilizar la funciones `authenticate` y `login`:__
   ```python
   from django.contrib.auth import authenticate, login
   from django.contrib.auth.decorators import login_required
   from django.shortcuts import render, redirect
   from .models import Usuario, Libro, Prestamo

   import datetime
   ```

   __Modificar la función login() de la sigiente manera:__
   ```python
   def login_user(request):
       """ Atiende las peticiones de GET /login/ """

       # Si hay datos vía POST se procesan
       if request.method == "POST":
           # Se obtienen los datos del formulario
           username = request.POST["username"]
           password = request.POST["password"]
           next = request.GET.get("next", "/")
           acceso = authenticate(username=username, password=password)
           if acceso is not None:
               # Se agregan datos al request para mantener activa la sesión
               login(request, acceso)
               # Y redireccionamos a next
               return redirect(next)
           else:
               # Usuario malo
               msg = "Datos incorrectos, intente de nuevo!"
       else:
           # Si no hay datos POST
           msg = ""
   [...]
   ```
   Como estamos importando la función `login()` de Django, tenemos que cambiar el nombre de nuestra función para que no entren en conflico, así que la renombramos a `login_user()`.

   __Ahora como cambiamos el nombre de la vista, hay que actualizar la ruta en `urls.py`:__
   ```python
   path("login/", views.login_user, name="login_user"),
   ```

   __Se agrega el decorador a la vista que necesita ser autenticada:__
   ```python
   @login_required()
   def nuevo_prestamo(request):
       """ Vista para atender la petción de la url /prestamo/nuevo/ """
       # Ahora queremos saber si hay o no petición POST primero
       if request.method == "POST":
   [...]
   ```

   __Se le indica a Django que la url para el login es `/login/` agregando la siguientes líneas al archivos `Biblioteca/Biblioteca/settings.py`:__
   ```python
   # Se define la URL para login
   LOGIN_URL = "/login/"
   ```

   Ahora cada vez que se abra la url `/prestamo/nuevo/` si no se está registrado en el sistema, no se podrá entrar a crear nuevos préstamos.

1. Modificando el archivo `base.html` para indicar cuando hay usuario activo o no.

   __Realizar las siguientes modificaciones al archivo `Biblioteca/catalogo/templates/base.html`:__
   ```html
   <ul>
       <li><a href="/prestamo/nuevo/">Nuevo préstamo</a></li>
       <li><a href="/">Libros prestados</a></li>
       {% if user.username == "" %}
       <li><a href="/login/">Login</a></li>
       {% else %}
       <li><a href="/logout/">{{ user.username }}</a></li>
       {% endif %}
   </ul>
   ```
   Las plantillas o archivos html siempre reciben la información del usuario actual activo.

__Felicidades!__ Otro éxito más, ya sólo falta un detalle así que mira el Reto-02 para resolverlo.
