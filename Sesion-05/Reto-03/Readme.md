`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 09`](../Readme.md) > Reto-03
## Usando las consultas junto a las plantillas de Django

### OBJETIVO
- Hacer uso del sistema de consultas de Django.
- Usar los resultados de las consultas en las plantillas de Django.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-05/Reto-03`
1. Diagrama del modelo entidad-relación para el proyect __Biblioteca__

   ![Modelo entidad-relación para Biblioteca](modelo-entidad-relacion.jpg)

1. Documentación de Django referente a modelos:
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/
   - Expresiones en consultas: https://docs.djangoproject.com/en/2.2/ref/models/expressions/
   - API de consultas https://docs.djangoproject.com/en/2.2/ref/models/querysets/

### DESARROLLO
1. Modificar la vista `index()` para que haga uso de las consultas de Django para obtener cada uno de los registros necesarios para mostrar en la tabla mostrada en el index.

   __Realizando cambios al archivo `Biblioteca/catalogo/views.py`:__
   ```python
   from .models import Usuario, Libro, Prestamo

   # Create your views here.
   def index(request):
       """ Vista para atender la petción de la url / """
       # Obteniendo los datos mediantes consultas
       prestamos = Prestamo.objects.all()
       # Generando una lista de registros resultado
       registros = []
       for p in prestamos:
           # Se obtienes los libros por cada préstamo
           for l in p.libros.all():
               d = {
                   "titulo":l.titulo,
                   "fechaPre":p.fechaPre,
                   "fechaDev":p.fechaDev,
                   "nombre":p.usuario.nombre
               }
               registros.append(d)

       return render(request, "catalogo/index.html", {"registros":registros})
   ```
   ***

1. Modificar la plantilla `index.html` para que haga uso de los resultados obtenidos en la vista:

   __Realizando cambios al archivo `Biblioteca/catalogo/template/catalogo/index.html`:__
   ```html
   <table class="table table-responsive table-hover table-striped ">
     <tr><th>Título</th><th>Fecha préstamo</th><th>Fecha devolución</th><th>Nombre</th></tr>
     {% for r in registros %}
     <tr>
       <td>{{ r.titulo }}</td>
       <td>{{ r.fechaPre }}</td>
       <td>{{ r.fechaDev }}</td>
       <td>{{ r.nombre }}</td>
     </tr>
     {% endfor %}
   </table>
   ```
   ***

__Resultado final:__

![Index dinámico](assets/index-01.png)
