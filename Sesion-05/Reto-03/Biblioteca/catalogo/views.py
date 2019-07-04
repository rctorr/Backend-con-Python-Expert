from django.shortcuts import render
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
