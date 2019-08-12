`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 07`](../Readme.md) > Ejemplo-02
## Creando un API GraphQL para realizar operaciones CRUD de una tabla

### OBJETIVOS
- Configurar __Django Graphene__
- Definir la url única para el acceso a todo el __API GraphQL__
- Integrar __Django Graphene__ en el proyecto
- Realizar operaciones de CRUD vía __API GraphQL__

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-06/Ejemplo-02`
1. Activar el entorno virtual __BeduTravels__
1. Diagrama de entidad-relación del proyecto BeduTravels

   ![Diagrama entidad-relación](assets/bedutravels-modelo-er.jpg)
1. Carpeta de proyecto 'Ejemplo-02/Bedutravels/' con los siguientes datos de acceso al admin de Django :
   - Usuario: bedutravels
   - Clave: bedutravels

### DESARROLLO
1. Agregando Django Graphene a la configuración en el archivo `settings.py` como una aplicación adicional:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'tours',
       'graphene_django',
   ]
   ```
   ***

1. Se crea la ruta para la url `/graphql` modificando el archivo `Bedutravels/tours/urls.py`:

   ```python
   from django.urls import path
   from graphene_django.views import GraphQLView

   urlpatterns = [
       path('graphql', GraphQLView.as_view(graphiql=True)),
   ]
   ```
   ***

1. Se crea la vista para el api de la tabla __Usuario__ aunque en este caso en lugar de generar y regresar HTML será JSON.

   __Abrimos el archivo `BeduTravels/catalogo/views.py` y agregar el siguiente contenido:__

   ```python
   # Imports
   from django.contrib.auth import authenticate, login, logout
   from django.contrib.auth.decorators import login_required
   from django.shortcuts import render, redirect

   from .models import Usuario, Libro, Prestamo
   from .serializers import UsuarioSerializer

   from rest_framework import viewsets

   import datetime

   [...al final agregar...]
   # Vistas basadas en clases para Django Rest
   class UsuarioViewSet(viewsets.ModelViewSet):
      """
      API que permite realizar operaciones en la tabla Usuario
      """
      # Se define el conjunto de datos sobre el que va a operar la vista,
      # en este caso sobre todos los usuarios disponibles.
      queryset = Usuario.objects.all().order_by('id')
      # Se define el Serializador encargado de transformar la peticiones
      # en formato JSON a objetos de Django y de Django a JSON.
      serializer_class = UsuarioSerializer
   ```
   ***

1. Se crea el serializador `UsuarioSerializer` en el archivo `BeduTravels/catalogo/serializers.py`.

   ```python
   from rest_framework import serializers

   from .models import Usuario

   class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
       """ Serializador para atender las conversiones para Usuario """
       class Meta:
           # Se define sobre que modelo actua
           model = Usuario
           # Se definen los campos a incluir
           fields = ('id', 'nombre', 'apellidos', 'edad', 'genero', 'direccion')
   ```
   ***

1. Acceso y uso de la __API__ `/api/usuarios`

   __Para tener acceso al API abrir la siguiente url:__

   http://localhost:8000/api/usuarios/

   Se deberá de observar algo similar a lo siguiente:

   ![BeduTravels API Usuarios](assets/api-usuarios-01.png)

   __Agregando un nuevo usuario vía web:__

   ![Agregando usuario vía web](assets/api-usuarios-02.png)

   ![Usuario agregado](assets/api-usuarios-03.png)

   __Agregando un nuevo usuario vía consola:__

   ```console
   (BeduTravels) Ejemplo-02 $ curl -d '{"nombre": "Donald", "apellidos": "Mac Pato", "edad": 101, "genero": "H", "direccion": ""}' -H 'Content-Type: application/json' http://localhost:8000/api/usuarios/
   {"id":6,"nombre":"Donald","apellidos":"Mac Pato","edad":101,"genero":"H","direccion":""}
   (BeduTravels) Ejemplo-02 $
   ```
   Notar que esto genera una petición POST y como resultado se obtiene el usuario agregado con el id asignado.

   También se puede verificar actualizando la lista de usuarios en la vista del api del navegador.

   __Eliminando el usuario Pluto vía consola:__

   ```console
   (BeduTravels) Ejemplo-02 $ curl -X DELETE http://localhost:8000/api/usuarios/5/

   (BeduTravels) Ejemplo-02 $
   ```
   Sin más el usuario se elimina y se puede verificar en la vista web.
