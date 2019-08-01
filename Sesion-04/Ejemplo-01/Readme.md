`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Ejemplo-01
## Creando una tabla con el modelo de datos de Django

### OBJETIVO
- Conocer y crear el modelo de datos con Django.
- Conocer el sistema de bases de datos usado por Django.
- Configurando Django para manejar datos regionales.
- Agregando el modelo al administrador de Django

#### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-04/Ejemplo-01`
1. Diagrama del modelo entidad-relación para el proyect __Biblioteca__

   ![Modelo entidad-relación para Biblioteca](modelo-entidad-relacion.jpg)

1. Documentación de Django referente a modelos:
   - Descripción de modelos y ejemplos: https://docs.djangoproject.com/en/2.2/topics/db/models/
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/
   - Referencia a los tipos de datos que maneja Django https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

#### DESARROLLO
1. Usando el modelo entidad-relación, crear cada modelo correspondiente a cada tabla.

   __Creando el modelo para la tabla Usuario agregando lo siguiente al archivo `Biblioteca/catalogo/models.ps`:__

   ```python
   from django.db import models

   # Create your models here.
   class Usuario(models.Model):
       """ Define la tabla Usuario """
       nombre = models.CharField(max_length=40)
       apellidos = models.CharField(max_length=80)
       edad = models.SmallIntegerField()
       GENERO_OPCIONES = [
           ("M", "Mujer"),
           ("H", "Hombre"),
       ]
       genero = models.CharField(max_length=1, choices=GENERO_OPCIONES)
       direccion = models.CharField(max_length=256, null=True, blank=True)
   ```

   __Nota:__ Django por omisión usa la base de datos SQLite3 y crea un archivo en la carpeta del proyecto con el nombre `db.sqlite3`.

   __Antes de continuar, tenemos que indicar a Django algunas configuraciones locales en el archivo `settings.py`:__

   ```python
   # Internationalization
   # https://docs.djangoproject.com/en/2.2/topics/i18n/

   LANGUAGE_CODE = 'es-MX'
   TIME_ZONE = 'America/Mexico_City'
   ```

   La lista tanto de códigos de lenguaje como de zonas horarias se puede consultar en:
   - http://www.i18nguy.com/unicode/language-identifiers.html
   - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

   __Avisando a Django que hemos modificado el archivo `models.py`:__

   ```console
   (Biblioteca) Ejemplo-01/Biblioteca $ python manage.py makemigrations
   Migrations for 'catalogo':
     catalogo/migrations/0001_initial.py
       - Create model Usuario

   (Biblioteca) Ejemplo-01/Biblioteca $ python manage.py migrate
   Operations to perform:
     Apply all migrations: admin, auth, catalogo, contenttypes, sessions
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     Applying admin.0002_logentry_remove_auto_add... OK
     Applying admin.0003_logentry_add_action_flag_choices... OK
     Applying contenttypes.0002_remove_content_type_name... OK
     Applying auth.0002_alter_permission_name_max_length... OK
     Applying auth.0003_alter_user_email_max_length... OK
     Applying auth.0004_alter_user_username_opts... OK
     Applying auth.0005_alter_user_last_login_null... OK
     Applying auth.0006_require_contenttypes_0002... OK
     Applying auth.0007_alter_validators_add_error_messages... OK
     Applying auth.0008_alter_user_username_max_length... OK
     Applying auth.0009_alter_user_last_name_max_length... OK
     Applying auth.0010_alter_group_name_max_length... OK
     Applying auth.0011_update_proxy_permissions... OK
     Applying catalogo.0001_initial... OK
     Applying sessions.0001_initial... OK

   (Biblioteca) Ejemplo-01/Biblioteca $
   ```

   __Django ya cuenta con un sistema CRUD para nuestros modelos y para activarlo es necesario agregar un usuario administrador cuando menos:__

   ```console
   (Biblioteca) Ejemplo-01/Biblioteca $ python manage.py createsuperuser
   Nombre de usuario (leave blank to use 'rctorr'): biblioteca
   Dirección de correo electrónico: biblioteca@gmail.com
   Password:
   Password (again):
   La contraseña es muy similar a  nombre de usuario.
   Bypass password validation and create user anyway? [y/N]: y
   Superuser created successfully.

   (Biblioteca) Ejemplo-01/Biblioteca $
   ```

   Abrir la url http://localhost:8000/admin y usar los siguientes datos para entrar:
   - Usuario: biblioteca
   - Clave: biblioteca
   - Email: biblioteca@gmail.com

   __Se deberá de ver algo similar a la siguiente imagen:__

   ![Django Admin](assets/django-admin-01.png)

   Pero nuestro modelo Usuario ¿dónde está?

   __Agregando el siguiente código al archivo `Biblioteca/catalogo/admin.py`:__

   ```python
   from django.contrib import admin
   from .models import Usuario

   # Register your models here.
   admin.site.register(Usuario)
   ```
   Actuaizamos el navegador se obtendrá lo siguiente:

   ![Django admin con modelo Usuario](assets/django-admin-02.png)

   Ahora ya se puede listar, agregar, actualizar o eliminar registros en la tabla Usuario.

   Diviértete!!!
