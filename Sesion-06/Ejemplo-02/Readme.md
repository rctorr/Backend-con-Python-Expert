`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 10`](../Readme.md) > Ejemplo-02
## Definiendo y agregando autenticación de entrada usando la vista auth_views.login de Django.

### OBJETIVO
- Crear autenticación de entrada usando la vista auth_views.login de Django.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Clase-10/Ejemplo-02`

### DESARROLLO
1. Modificar la ruta `/login` para hacer uso de la vista

   __Se modifica el archivo `Biblioteca/catalogo/urls.py` con los siguientes imports:__
   ```python
   from django.contrib.auth import views as auth_views
   ```

   __Se modifica la ruta:__
   ```python
   path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
   ```
   Notar que se usa la misma plantilla login.html que ya se tenía, pero lo más importante es que no se necesita crear en este caso una vista, incluso se puede borrar la vista `login_user()`.

   __Borra la vista `login_user() del archivos views.py`__

    Verifica que el proceso de login y logout sigue funcionando

Esto está bien si no se necesita personalizar el proceso de login, de lo contrario si es necesario crear el proceso a mano.
