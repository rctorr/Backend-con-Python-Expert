`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 04`](../Readme.md) > Ejemplo-04
## El sistema de plantillas de Django

### OBJETIVO
- Hacer uso del sistema de consultas de Django.
- Conocer el sistemas de plantillas de Django
- Aplicar las consultas en las plantillas de Django.

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Sesion-04/Ejemplo-04`
1. Diagrama del modelo entidad-relación para el proyecto __Bedutravels__

   ![Modelo entidad-relación para Bedutravels](bedutravels-modelo-er.png)

1. Documentación de Django referente a modelos:
   - Referencia a la API de Modelos en Django https://docs.djangoproject.com/en/2.2/ref/models/
   - Expresiones en consultas: https://docs.djangoproject.com/en/2.2/ref/models/expressions/
   - API de consultas https://docs.djangoproject.com/en/2.2/ref/models/querysets/

### DESARROLLO
1. Modificar la vista `index()` para que haga uso de las consultas de Django para obtener cada uno de los registros necesarios para mostrar en la lista de Tours

   __Realizando cambios al archivo `Bedutravels/tours/views.py`:__
   ```python
   from .models import Zona, Tour

   # Create your views here.
   def index(request):
       """ Vista para atender la petción de la url / """
       # Obteniendo los datos mediantes consultas
       tours = Tour.objects.all()

       return render(request, "tours/index.html", {"tours":tours})
   ```
   ***

1. Modificar la plantilla `index.html` para que haga uso de los resultados obtenidos en la vista:

   __Realizando cambios al archivo `Bedutravels/tours/template/tours/index.html`:__
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
