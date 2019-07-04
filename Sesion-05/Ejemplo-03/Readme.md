`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 09`](../Readme.md) > Ejemplo-03
## Definiendo las consultas usando el ORM de Django

### OBJETIVO
- Conocer y comprender el sistema de consultas o Object Relacional Mapping (ORM) de Django.
- Conocer las consultas entre tablas y sus relaciones
- Definir una consulta para generar un reporte.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-05/Ejemplo-03`
1. Diagrama del modelo entidad-relación para el proyect __Biblioteca__

   ![Modelo entidad-relación para Biblioteca](modelo-entidad-relacion.jpg)

1. Documentación de Django referente a modelos:
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/

### DESARROLLO
1. Usando el __Shell de Django__ mostrar todos los registros de la tabla Libro:

   __Iniciando el Shell de Django:__
   ```console
   (Biblioteca) Ejemplo-03/Biblioteca $ python manage.py shell
   Python 3.7.3 (default, Mar 27 2019, 22:11:17)
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   (InteractiveConsole)
   >>>
   ```

   __Realizando la consulta para obtener todos los registros de la tabla Libro:__

   ```python
   >>> from catalogo.models import Libro
   >>> Libro.objects.all()
   <QuerySet [<Libro: Yo, Robot>, <Libro: El fin de la eternidad>, <Libro: El arte de la guerra>]>
   >>>
   ```
   ***

1. Imprime los datos del libro con `id = 3`:

   __Dentro el Shell de Django:__

   ```python
   >>> l3 = Libro.objects.get(pk=3)
   >>> l3
   <Libro: El arte de la guerra>
   >>> print(l3.id, l3.titulo, l3.editorial, l3.numPag, l3.autores)
   3 El arte de la guerra Obelisco 112 1
   >>>
   ```
   ***

1. Imprime los préstamos del usuario __Hugo__ haciendo uso de la relacion uno a muchos entre Prestamo y Usuario:

   __Dentro el Shell de Django:__

   ```python
   >>> from catalogo.models import Prestamo
   >>> Prestamo.objects.filter(usuario__nombre="Hugo")
   <QuerySet [<Prestamo: 1>, <Prestamo: 4>]>
   ```
   ***

1. Imprime la lista de todos los libros prestados al usuario __Hugo__ incluyendo nombre de usuario, libros prestados y fecha de préstamo de cada libro.

   __Dentro el Shell de Django:__

   ```python
   >>> from catalogo.models import Usuario, Libro, Prestamo
   >>> u1 = Usuario.objects.get(nombre="Hugo")
   >>> u1
   <Usuario: Hugo Mac Rico>
   >>> prestamos = Prestamo.objects.filter(usuario=u1)
   >>> prestamos
   <QuerySet [<Prestamo: 1>, <Prestamo: 4>]>
   >>> for p in prestamos:
   ...     for l in p.libros.all():
   ...         reg = (u1.nombre, l.titulo, p.fechaPre)
   ...         print(reg)
   ...
   ('Hugo', 'Yo, Robot', datetime.date(2019, 6, 24))
   ('Hugo', 'El arte de la guerra', datetime.date(2019, 6, 24))
   ('Hugo', 'El fin de la eternidad', datetime.date(2019, 6, 24))
   >>>
   ```
   ***
