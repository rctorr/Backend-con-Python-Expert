`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 02`](../Readme.md) > Reto-02

## Realizar la operación Read a una tabla con Python en un servidor MariaDB.

### OBJETIVO
Realizar la operación __Read__ a una tabla con Python en un servidor MariaDB para el proyecto BeduTravels.

#### REQUISITOS
1. Contar con los datos de conexión a la base de datos BeduTravels.

   __Host:__ localhost <br />
   __User:__ BeduTravels <br />
   __Password:__ BeduTravels <br />
   __Base de datos:__ BeduTravels

1. Usar la carpeta de trabajo `Sesion-02/Reto-02/`

1. Contar con la definición de la tabla __Usuario__ y con varios registros ya en la base de datos BeduTravels.

   ![Tabla Usuario](assets/tabla-usuario.jpg)

   En caso de no contar con la tabla o los registros, entonces inicializar la tabla usando el archivo `Sesion-02/Reto-02/sql/tabla-usuario.sql`

### DESARROLLO
1. __OPERACIÓN READ__ Realizar las modificaciones necesarias en los scripts `lista-registros.py` y `modelomysql.py` para que se imprima en la salida estándar la lista de registros de la tabla proporcionada por el usuario:

   __Caso: Ejecutando el script sin argumentos__

   ```console
   Sesion-02/Reto-02 $ python lista-registros.py

   Tablas disponibles
   ------------------
   Usuario
   ------------------
   ```

   __Caso: Imprimiendo registros de la tabla Usuario__

   ```console
   Sesion-02/Reto-02 $ python lista-registros.py Usuario

   Tabla: Usuario
   --------------
   Id | Nombre | Apellidos | Edad | Genero
    1 | Hugo   | Mac Rico  |   10 | M     
    2 | Paco   | Mac Rico  |   15 | M     
    3 | Daisy  | Mac Rico  |   18 | H     
   --------------
   ```
   ***

__Nota:__ Este reto se realiza en 3 mins o menos.
