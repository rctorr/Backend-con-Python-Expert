from django.shortcuts import render
from .models import Usuario, Libro, Prestamo

import datetime

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

def nuevo_prestamo(request):
    """ Vista para atender la petción de la url /prestamo/nuevo/ """
    # Ahora queremos saber si hay o no petición POST primero
    if request.method == "POST":
        idUsuario = request.POST["idUsuario"]
        idUsuario = int(idUsuario)
        idLibro1 = request.POST["idLibro1"]
        idLibro2 = request.POST["idLibro2"]
        idLibro3 = request.POST["idLibro3"]
        idLibro4 = request.POST["idLibro4"]
        idLibro5 = request.POST["idLibro5"]

        usuario = Usuario.objects.get(pk=idUsuario)
        prestamo = Prestamo(usuario=usuario, fechaPre=datetime.date.today())
        prestamo.save()
        if idLibro1 is not "0":
            idLibro1 = int(idLibro1)
            libro1 = Libro.objects.get(pk=idLibro1)
            prestamo.libros.add(libro1)
        print(idLibro2)
        if idLibro2 is not "0":
            idLibro2 = int(idLibro2)
            libro2 = Libro.objects.get(pk=idLibro2)
            prestamo.libros.add(libro2)
        if idLibro3 is not "0":
            idLibro3 = int(idLibro3)
            libro3 = Libro.objects.get(pk=idLibro3)
            prestamo.libros.add(libro3)
        if idLibro4 is not "0":
            idLibro4 = int(idLibro4)
            libro4 = Libro.objects.get(pk=idLibro4)
            prestamo.libros.add(libro4)
        if idLibro5 is not "0":
            idLibro5 = int(idLibro5)
            libro5 = Libro.objects.get(pk=idLibro5)
            prestamo.libros.add(libro5)
        prestamo.save()
        msg = "Prestamo guardado con éxito!"
    else:
        msg = ""

    # Inicialmente lo que queremos es ver el formulario
    usuarios = Usuario.objects.all()
    fecha = datetime.date.today().strftime("%d-%m-%Y")
    libros = Libro.objects.all()

    return render(request, "catalogo/nuevo-prestamo.html",
        {
            "usuarios":usuarios,
            "fecha":fecha,
            "libros":libros,
            "msg":msg
        }
    )
