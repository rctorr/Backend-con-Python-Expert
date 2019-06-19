`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Reto-01
## Entornos virtuales e instalación de Django

### OBJETIVO
- Crear un entorno virtual para el proyecto BeduTravels
- Restaurar entorno virtual

#### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-04/Reto-01`

#### DESARROLLO
1. Crear un entorno virtual para el proyecto BeduTravels con Django usando el comando:

   ```console
   Sesion-04/Reto-01 $ conda create --name BeduTravels python=3.7
   Solving environment: done

   ## Package Plan ##

     environment location: /home/rctorr/miniconda3/envs/BeduTravels

     added / updated specs:
       - python=3.7

   The following packages will be downloaded:

       package                    |            build
       ---------------------------|-----------------
       pip-19.1.1                 |           py37_0         1.8 MB
       certifi-2019.3.9           |           py37_0         155 KB
       libgcc-ng-9.1.0            |       hdf63c60_0         8.1 MB
       setuptools-41.0.1          |           py37_0         648 KB
       openssl-1.1.1c             |       h7b6447c_1         3.8 MB
       libstdcxx-ng-9.1.0         |       hdf63c60_0         4.0 MB
       python-3.7.3               |       h0371630_0        36.7 MB
       wheel-0.33.4               |           py37_0          39 KB
       sqlite-3.28.0              |       h7b6447c_0         1.9 MB
       ca-certificates-2019.5.15  |                0         133 KB
       ------------------------------------------------------------
                                              Total:        57.2 MB

   The following NEW packages will be INSTALLED:

       ca-certificates: 2019.5.15-0            
       certifi:         2019.3.9-py37_0        
       libedit:         3.1.20181209-hc058e9b_0
       libffi:          3.2.1-hd88cf55_4       
       libgcc-ng:       9.1.0-hdf63c60_0       
       libstdcxx-ng:    9.1.0-hdf63c60_0       
       ncurses:         6.1-he6710b0_1         
       openssl:         1.1.1c-h7b6447c_1      
       pip:             19.1.1-py37_0          
       python:          3.7.3-h0371630_0       
       readline:        7.0-h7b6447c_5         
       setuptools:      41.0.1-py37_0          
       sqlite:          3.28.0-h7b6447c_0      
       tk:              8.6.8-hbc83047_0       
       wheel:           0.33.4-py37_0          
       xz:              5.2.4-h14c3975_4       
       zlib:            1.2.11-h7b6447c_3      

   Proceed ([y]/n)? y

   Downloading and Extracting Packages
   pip-19.1.1           | 1.8 MB    | ##################################### | 100%
   certifi-2019.3.9     | 155 KB    | ##################################### | 100%
   libgcc-ng-9.1.0      | 8.1 MB    | ##################################### | 100%
   setuptools-41.0.1    | 648 KB    | ##################################### | 100%
   openssl-1.1.1c       | 3.8 MB    | ##################################### | 100%
   libstdcxx-ng-9.1.0   | 4.0 MB    | ##################################### | 100%
   python-3.7.3         | 36.7 MB   | ##################################### | 100%
   wheel-0.33.4         | 39 KB     | ##################################### | 100%
   sqlite-3.28.0        | 1.9 MB    | ##################################### | 100%
   ca-certificates-2019 | 133 KB    | ##################################### | 100%
   Preparing transaction: done
   Verifying transaction: done
   Executing transaction: done
   #
   # To activate this environment, use:
   # > source activate BeduTravels
   #
   # To deactivate an active environment, use:
   # > source deactivate
   #

   Sesion-04/Reto-01 $
   ```

   __Dejar activo el entorno BeduTravels para continuar:__

   ```console
   Sesion-04/Reto-01 $ source activate BeduTravels

   (BeduTravels) Sesion-04/Reto-01 $
   ```
   ***

1. Restaurando el entorno virtual para el proyecto BeduTravels

   __Para restaurar un entorno virtual se realiza con:__

   ```console
   (BeduTravels) Sesion-04/Reto-01 $ pip install -r requeriments.txt
   Requirement already satisfied: certifi==2019.3.9 in /home/rctorr/miniconda3/envs/BeduTravels/lib/python3.7/site-packages (from -r requeriments.txt (line 1)) (2019.3.9)
   Collecting Django==2.2.2 (from -r requeriments.txt (line 2))
     Using cached https://files.pythonhosted.org/packages/eb/4b/743d5008fc7432c714d753e1fc7ee56c6a776dc566cc6cfb4136d46cdcbb/Django-2.2.2-py3-none-any.whl
   Collecting pytz==2019.1 (from -r requeriments.txt (line 3))
     Using cached https://files.pythonhosted.org/packages/3d/73/fe30c2daaaa0713420d0382b16fbb761409f532c56bdcc514bf7b6262bb6/pytz-2019.1-py2.py3-none-any.whl
   Collecting sqlparse==0.3.0 (from -r requeriments.txt (line 4))
     Using cached https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
   Installing collected packages: pytz, sqlparse, Django
   Successfully installed Django-2.2.2 pytz-2019.1 sqlparse-0.3.0

   (BeduTravels) Sesion-04/Reto-01 $
   ```

   __Para mostrar la lista de módulos instalados:__

   ```console
   (BeduTravels) Sesion-04/Reto-01 $ pip freeze
   certifi==2019.3.9
   Django==2.2.2
   pytz==2019.1
   sqlparse==0.3.0

   (BeduTravels) Sesion-04/Reto-01 $
   ```

   Ahora estamos listos para continuar con Django.
   ***
