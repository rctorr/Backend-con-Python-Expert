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
   ???
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
   ???
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
   ???
   ```
   Considera que para modificar un __Tour__ necesitamos saber cual y para ello se requiere del __id__.

   En el caso de modificar las zonas, considerar que es una relación a la tabla Zona, por lo que hay que buscar la zona con el nuevo id.

   __Se agrega a la clase de la lista de mutaciones:__

   ```python
   class Mutaciones(graphene.ObjectType):
       crear_zona = CrearZona.Field()
       eliminar_zona = EliminarZona.Field()
       modificar_zona = ModificarZona.Field()
       crear_tour = CrearTour.Field()
       modificar_tour = ModificarTour.Field()
   ```

1. Se agrega un nuevo __Tour__ usando los siguientes datos:

   - Nombre: Yacatas
   - Slug: mexico
   - Operador: Mochilazo
   - Tipo de tour: Tour en grupo
   - Descripción: Templos religiosos del Imperio Tarascan, rivales a los Aztecas
   - pais: México
   - Zona de salida: Ciudad de México
   - Zona de llegada: Michoacán

   __La mutación en GraphQL es:__

   ```json
   ???
   ```

   __Modificando el tour anterior agregando la url de la imagen:__

   - Imágen: https://i.imgur.com/jJuy1vU.jpg

   ```json
   mutation ModificarTour {
     modificarTour(
       id:"5",
       img:"https://i.imgur.com/jJuy1vU.jpg"
     ) {
       tour {
         id
         nombre
         img
       }
     }
   }
   ```

   __Obteniendo un resultado similar a:__

   ```json
   {
     "data": {
       "modificarTour": {
         "tour": {
           "id": "5",
           "nombre": "Yacatas",
           "img": "https://i.imgur.com/jJuy1vU.jpg"
         }
       }
     }
   }
   ```
   ***

1. Se crea la operación eliminar para la tabla __Tour__

   __Se crea la mutación en el archivo `Bedutravels/tours/schema.py`:__

   ```python
   ???
   ```
   Considera que para eliminar un __Tour__ necesitamos saber cual y para ello se requiere del __id__.

   Como el tour será eliminado, no se puede regresar como valor, por esa razón se usa la variable __ok__ para indicar el estado de la operación.

   __Se agrega a la clase de la lista de mutaciones:__

   ```python
   class Mutaciones(graphene.ObjectType):
       crear_zona = CrearZona.Field()
       eliminar_zona = EliminarZona.Field()
       modificar_zona = ModificarZona.Field()
       crear_tour = CrearTour.Field()
       modificar_tour = ModificarTour.Field()
       eliminar_tour = EliminarTour.Field()
   ```

1. Se agrega un nuevo __Tour__ usando los siguientes datos:

   - Nombre: Luciérnas salvajes
   - Descripción: Viven en carne propia ser perseguido y devorado por miles de Luciérnagas.
   - Zona de salida: Ciudad de México
   - Zona de llegada: Yucatán

   __La mutación en GraphQL es:__

   ```json
   ???
   ```

   __Eliminando el tour anterior:__

   ```json
   mutation EliminarTour {
     eliminarTour(id:"6") {
       ok
     }
   }
   ```

   __Obteniendo un resultado similar a:__

   ```json
   {
     "data": {
       "eliminarTour": {
         "ok": true
       }
     }
   }
   ```
   ***
