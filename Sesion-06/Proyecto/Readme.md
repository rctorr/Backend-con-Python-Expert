`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 06`](../Readme.md) > Proyecto
## Creando un API para realizar las operaciones CRUD de una tabla

### OBJETIVOS
- Agregar la relación entre los modelos __Tour__ y __Salida__.
- Realizar operaciones de CRUD vía API para la tabla __Salida__ incluyendo los tours asociados.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-06/Proyecto`
1. Activar el entorno virtual __Bedutravels__
1. Diagrama de entidad-relación del proyecto Bedutravels

   ![Diagrama entidad-relación](assets/bedutravels-modelo-er.png)

### DESARROLLO
1. Se actualiza el serializador `TourSerializer` en el archivo `Bedutravels/tours/serializers.py` para agregar el campo `salidas` para que muestre la lista de salidas por cada tour:

   ```python        
           # Se definen los campos a incluir
           fields = ('id', 'slug', 'nombre', 'operador', 'tipoDeTour',
               'descripcion', 'img', 'pais', 'zonaSalida', 'zonaLlegada',
               'salidas')
   ```
   ***

1. Acceso y uso de la __API__ `/api/tours`

   __Para tener acceso al API abrir la siguiente url:__

   http://localhost:8000/api/tours/

   Se deberá de observar algo similar a lo siguiente:

   ![bedutravels API tours](assets/api-tours-01.png)

   __Para tener acceso al detalle del tour con id=1 abrir la siguiente url:__

   http://localhost:8000/api/tour/1/

   Se deberá de observar algo similar a lo siguiente:

   ![bedutravels API tour](assets/api-tours-02.png)
   ***

1. Ahora se modifica nuevamente el archivo `serializers.py` para que se muestre la lista de salidas por cada tour.

   ```python
   class SalidaSerializer(serializers.HyperlinkedModelSerializer):
      """ Serializador para atender las conversiones para Salida """

      # Se define la relación muchos a muchos entre Libro y Salida
      tour = TourSerializer(many=True, read_only=True)
      class Meta:
          # Se define sobre que modelo actua
          model = Salida
          # Se definen los campos a incluir
          fields = ('id', 'fechaInicio', 'fechaFin', 'asientos', 'precio', 'tour')
   ```

   __El resultado debe ser como el siguiente:__

   ![Lista de tours con salidas incluídos](assets/api-tours-03.png)
