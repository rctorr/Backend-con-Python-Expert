`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 10`](../Readme.md) > Reto-02
## Definiendo y agregando autenticación de entrada usando la vista auth_views.login de Django.

### OBJETIVO
- Crear autenticación de salida usando la vista auth_views.logout de Django.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Clase-10/Reto-02`

### DESARROLLO
1. Modificar la ruta `/logout` para hacer uso de la vista

   __Se modifica la ruta:__
   ```python
   path("logout/", auth_views.logoutView.as_view(next_page="/"), name="logout"),
   ```
   De igual forma no se requiere la la vista `logout_user()`.

   __Borra la vista `logout_user() del archivos views.py`__

    Verifica que el proceso de login y logout sigue funcionando

1. Corrigiendo un bug al usar __Login__ desde el menú

   __Modificar el archivo `Biblioteca/catalogo/template/registration/login.html`:__
   ```html
   {% if next %}
   <input type="hidden" name="next" value="{{ next }}" />
   {% else %}
   <input type="hidden" name="next" value="/" />
   {% endif %}
   ```
