##### POSTWORK
## BASES DE DATOS SQL EN PYTHON APLICADO A PROYECTO PERSONAL

### OBJETIVOS
 - Inicializar un contenedor con un servidor de base de datos MariaDB.
 - Inicializar la base de datos.
 - Inicializar las tablas y datos.
 - Listar los registros de una tabla desde un script en Python.
 - Agregar registros a una tabla haciendo uso de un script en Python.

#### REQUISITOS
1. Contar con la descripción del proyecto en no más de una cuartilla.
1. Contar con un diagrama del modelo entidad-relación.
1. Usar la carpeta de trabajo `Sesion-02/Postwork`

   ```console
   $ cd Sesion-02/Postwork

   Sesion-02/Postwork $
   ```

### DESARROLLO
1. __INICIALIZAR LA BASE DE DATOS__ Este paso es muy similar al realizado en el Reto-01, sólo que en lugar de usar el archivo `bedutravels.sql`, ahora se usará el archivo `sql/proyecto.sql`.

  __Comando a ejecutar para el caso de Docker en Linux o Mac:__
  ```sh
  Sesion-02/Postwork $ sudo docker exec -i pythonsql mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```

  __Comando a ejecutar para el caso de Docker en Windows:__
  ```sh
  Sesion-02/Postwork > docker exec -i pythonsql mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```

  __Comando a ejecutar para el caso de MySQL:__
  ```sh
  Sesion-02/Postwork $ mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```
  ***

1. __INICIALIZACIÓN DE TABLAS__ Para este paso seguir las instrucciones del Postwork pero usando el archivo `sql/tablas-proyecto.sql`.

   __Realizando la inicialización con:__
   ```console
   Sesion-02/Postwork $ sudo docker exec -i pythonsql mysql -hlocalhost -uProyecto -pProyecto Proyecto < sql/tablas-proyecto.sql

   Sesion-02/Postwork $
   ```
   ***

1. __OPERACIÓN READ__ Realizar las modificaciones necesarias en los scripts `lista-registros.py` y `modelomysql.py` para que se imprima en la salida estándar la lista de registros de una o más tablas proporcionada por el usuario:

   __Caso: Ejecutando el script sin argumentos__

   ```console
   Sesion-02/Postwork $ python lista-registros.py

   Tablas disponibles
   ------------------
   ???
   ???
   ------------------
   ```

   __Caso: Imprimiendo registros de la tabla ???__

   ```console
   Sesion-02/Postwork $ python lista-registros.py ???

   Tabla: ???
   --------------
   ???
   --------------
   ```
   ***
