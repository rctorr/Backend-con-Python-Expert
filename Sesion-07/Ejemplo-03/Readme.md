`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 11`](../Readme.md) > Ejemplo-03
## Creando un API para realizar las operaciones CRUD de una tabla con relaciones uno a muchos.

### OBJETIVOS
- Agregar el modelo __Prestamo__ a el __API__ de la Biblioteca
- Realizar operaciones de CRUD vía API para la tabla __Prestamo__

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-07/Ejemplo-03`
1. Activar el entorno virtual __Biblioteca__
1. Diagrama de entidad-relación del proyecto Biblioteca

   ![Diagrama entidad-relación](assets/biblioteca-diagrama-modelo-er.jpg)

### DESARROLLO
1. Se crea la ruta para la url `/api/prestamos` modificando el archivo `Biblioteca/catalogo/urls.py`:

   ```python
   router.register(r'prestamos', views.PrestamoViewSet)
   ```
   ***

1. Se crea la vista para el api de la tabla __Prestamo__ aunque en este caso en lugar de generar y regresar HTML será JSON.

   __Abrimos el archivo `Biblioteca/catalogo/views.py` y agregar el siguiente contenido:__

   ```python
   from .serializers import UsuarioSerializer, LibroSerializer ,PrestamoSerializer

   [...al final agregar...]
   class PrestamoViewSet(viewsets.ModelViewSet):
      """
      API que permite realizar operaciones en la tabla Prestamo
      """
      # Se define el conjunto de datos sobre el que va a operar la vista,
      # en este caso sobre todos los prestamos disponibles.
      queryset = Prestamo.objects.all().order_by('id')
      # Se define el Serializador encargado de transformar la peticiones
      # en formato JSON a objetos de Django y de Django a JSON.
      serializer_class = PrestamoSerializer
   ```
   ***

1. Se crea el serializador `PrestamoSerializer` en el archivo `Biblioteca/catalogo/serializers.py`.

   ```python
   from .models import Usuario, Libro, Prestamo

   class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
       """ Serializador para atender las conversiones para Prestamo """
       class Meta:
           # Se define sobre que modelo actua
           model = Prestamo
           # Se definen los campos a incluir
           fields = ('id', 'usuario', 'fechaPre', 'fechaDev')

   class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
       """ Serializador para atender las conversiones para Usuario """

       # Se define la relación de un usuario y sus préstamos realizados
       prestamos = PrestamoSerializer(many=True, read_only=True)

       class Meta:
           # Se define sobre que modelo actua
           model = Usuario
           # Se definen los campos a incluir
           fields = ('id', 'nombre', 'apellidos', 'edad', 'genero',
               'direccion', 'prestamos')
   ```
   __Nota:__ Es importante el nuevo orden de las clases

   __Se realiza la siguiente modificación al modelo Prestamo en el archivos `Biblioteca/catalogo/models.py`:__

   ```python
   class Prestamo(models.Model):
       """ Define la tabla Prestamo """
       usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="prestamos")
   ```
   Este cambio permite hacer un seguimiento desde un usuario hacía sus prestamos relacionados.
   ***

1. Acceso y uso de la __API__ `/api/prestamos`

   __Para tener acceso al API abrir la siguiente url:__

   http://localhost:8000/api/prestamos/

   Se deberá de observar algo similar a lo siguiente:

   ![biblioteca API Prestamos](assets/api-prestamos-01.png)

   __Para tener acceso a la lista de prestamos del usuario con id=1 abrir la siguiente url:__

   http://localhost:8000/api/usuarios/1/

   Se deberá de observar algo similar a lo siguiente:

   ![biblioteca API Prestamos](assets/api-prestamos-02.png)
