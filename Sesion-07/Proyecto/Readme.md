[`Backend con Python`](../../Readme.md) > [`Sesión 07`](../Readme.md) > Proyecto
## Creando una API GraphQL con todas las operaciones CRUD sobre una tabla

### OBJETIVOS
- Aplicar el concepto de mutaciones de GraphQL
- Crear una mutación para cada operación CRUD para la tabla Tour

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-07/Proyecto`
1. Activar el entorno virtual __Bedutravels__
1. Diagrama de entidad-relación del proyecto Bedutravels
   ![Diagrama entidad-relación](assets/bedutravels-modelo-er.png)

### DESARROLLO
1. La operación de lectura (read) o consultas ya se ha realizado con anterioridad, así que se puede continuar con la operación de agregar (create).

1. Se crea la operación agregar nuevo registros a la __API GraphQL__ para la tabla __Tour__

   __Se crea la mutación en el archivo `Bedutravels/tours/schema.py`:__

   ```python
   class CrearTour(graphene.Mutation):
       """ Permite realizar la operación de crear en la tabla Tour """

       class Arguments:
           """ Define los argumentos para crear un Tour """
           nombre = graphene.String(required=True)
           descripcion = graphene.String(required=True)
           idZonaSalida = graphene.ID(required=True)
           idZonaLlegada = graphene.ID(required=True)
           slug = graphene.String()
           operador = graphene.String()
           tipoDeTour = graphene.String()
           img = graphene.String()
           pais = graphene.String()

       # El atributo usado para la respuesta de la mutación
       tour = graphene.Field(TourType)

       def mutate(self, info, nombre, descripcion, idZonaSalida, idZonaLlegada,
           slug=None, operador=None, tipoDeTour=None, img=None, pais=None):
           """
           Se encarga de crear un nuevo Tour

           Los atributos obligatorios son:
           - nombre
           - descripcion
           - idZonaSalida
           - idZonaLlegada

           Los atributos opcionales son:
           - slug
           - operador
           - tipoDeTour
           - img
           - pais
           """
           zonaSalida = Zona.objects.get(pk=idZonaSalida)
           zonaLlegada = Zona.objects.get(pk=idZonaLlegada)
           tour = Tour(
               nombre=nombre,
               descripcion=descripcion,
               zonaSalida=zonaSalida,
               zonaLlegada=zonaLlegada,
               slug=slug,
               operador=operador,
               tipoDeTour=tipoDeTour,
               img=img,
               pais=pais
           )
           tour.save()

           # Se regresa una instancia de esta mutación
           return CrearTour(tour=tour)
   ```
   No olvidar colocar la opción `required=True` para los argumentos obligatorios, así como en el método `mutate()` indicar los argumentos opciones con valor `None`.

   Considerar que la tabla __Tour__ está relacionada con la tabla __Zona__, así que para crear un nuevo tour, es necesario primero obtener las zonas relacionadas.

   __Se agrega a la clase de la lista de mutaciones:__

   ```python
   class Mutaciones(graphene.ObjectType):
       crear_zona = CrearZona.Field()
       eliminar_zona = EliminarZona.Field()
       modificar_zona = ModificarZona.Field()
       crear_tour = CrearTour.Field()
   ```

1. Se agrega un nuevo __Tour__ usando los siguientes datos:

   - Nombre: Purepecha
   - Slug: mexico
   - Operador: Mochilazo
   - Tipo de tour: Tour en grupo
   - Descripción: Descubre las historias milenarias de los Purepecha
   - img: https://i.imgur.com/vVq652d.jpg
   - pais: México
   - Zona de salida: Ciudad de México
   - Zona de llegada: Michoacán

   __La mutación en GraphQL es:__

   ```json
   mutation CrearTour {
     crearTour(
       nombre:"Purepecha",
       slug:"mexico",
       operador:"Mochilazo",
       tipoDeTour:"Tour en grupo",
       descripcion:"Descubre las historias milenarias de los Purepechas",
       img:"https://i.imgur.com/vVq652d.jpg",
       pais:"México",
       idZonaSalida:"1",
       idZonaLlegada:"12"
     ) {
       tour {
         id
         nombre
         descripcion
         zonaSalida {
           id
           nombre
         }
         zonaLlegada {
           id
           nombre
         }
       }
     }
   }
   ```
   __Obteniendo un resultado similar a:__

   ```json
   {
     "data": {
       "crearTour": {
         "tour": {
           "id": "4",
           "nombre": "Purepecha",
           "descripcion": "Descubre las historias milenarias de los Purepechas",
           "zonaSalida": {
             "id": "1",
             "nombre": "Ciudad de México"
           },
           "zonaLlegada": {
             "id": "12",
             "nombre": "Michoacán"
           }
         }
       }
     }
   }   
   ```
   ***

1. Se crea la operación modificar para la tabla __Tour__

   __Se crea la mutación en el archivo `Bedutravels/tours/schema.py`:__

   ```python
   class CrearTour(graphene.Mutation):
       """ Permite realizar la operación de crear en la tabla Tour """

       class Arguments:
           """ Define los argumentos para crear un Tour """
           nombre = graphene.String(required=True)
           descripcion = graphene.String(required=True)
           idZonaSalida = graphene.ID(required=True)
           idZonaLlegada = graphene.ID(required=True)
           slug = graphene.String()
           operador = graphene.String()
           tipoDeTour = graphene.String()
           img = graphene.String()
           pais = graphene.String()

       # El atributo usado para la respuesta de la mutación
       tour = graphene.Field(TourType)

       def mutate(self, info, nombre, descripcion, idZonaSalida, idZonaLlegada,
           slug=None, operador=None, tipoDeTour=None, img=None, pais=None):
           """
           Se encarga de crear un nuevo Tour

           Los atributos obligatorios son:
           - nombre
           - descripcion
           - idZonaSalida
           - idZonaLlegada

           Los atributos opcionales son:
           - slug
           - operador
           - tipoDeTour
           - img
           - pais
           """
           zonaSalida = Zona.objects.get(pk=idZonaSalida)
           zonaLlegada = Zona.objects.get(pk=idZonaLlegada)
           tour = Tour(
               nombre=nombre,
               descripcion=descripcion,
               zonaSalida=zonaSalida,
               zonaLlegada=zonaLlegada,
               slug=slug,
               operador=operador,
               tipoDeTour=tipoDeTour,
               img=img,
               pais=pais
           )
           tour.save()

           # Se regresa una instancia de esta mutación
           return CrearTour(tour=tour)
   ```
   No olvidar colocar la opción `required=True` para los argumentos obligatorios, así como en el método `mutate()` indicar los argumentos opciones con valor `None`.

   Considerar que la tabla __Tour__ está relacionada con la tabla __Zona__, así que para crear un nuevo tour, es necesario primero obtener las zonas relacionadas.

   __Se agrega a la clase de la lista de mutaciones:__

   ```python
   class Mutaciones(graphene.ObjectType):
       crear_zona = CrearZona.Field()
       eliminar_zona = EliminarZona.Field()
       modificar_zona = ModificarZona.Field()
       crear_tour = CrearTour.Field()
   ```

1. Se agrega un nuevo __Tour__ usando los siguientes datos:

   - Nombre: Purepecha
   - Slug: mexico
   - Operador: Mochilazo
   - Tipo de tour: Tour en grupo
   - Descripción: Descubre las historias milenarias de los Purepecha
   - img: https://i.imgur.com/vVq652d.jpg
   - pais: México
   - Zona de salida: Ciudad de México
   - Zona de llegada: Michoacán

   __La mutación en GraphQL es:__

   ```json
   mutation CrearTour {
     crearTour(
       nombre:"Purepecha",
       slug:"mexico",
       operador:"Mochilazo",
       tipoDeTour:"Tour en grupo",
       descripcion:"Descubre las historias milenarias de los Purepechas",
       img:"https://i.imgur.com/vVq652d.jpg",
       pais:"México",
       idZonaSalida:"1",
       idZonaLlegada:"12"
     ) {
       tour {
         id
         nombre
         descripcion
         zonaSalida {
           id
           nombre
         }
         zonaLlegada {
           id
           nombre
         }
       }
     }
   }
   ```
   __Obteniendo un resultado similar a:__

   ```json
   {
     "data": {
       "crearTour": {
         "tour": {
           "id": "4",
           "nombre": "Purepecha",
           "descripcion": "Descubre las historias milenarias de los Purepechas",
           "zonaSalida": {
             "id": "1",
             "nombre": "Ciudad de México"
           },
           "zonaLlegada": {
             "id": "12",
             "nombre": "Michoacán"
           }
         }
       }
     }
   }   
   ```
   ***
