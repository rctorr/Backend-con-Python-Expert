from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Usuario, Libro, Prestamo
from .serializers import UsuarioSerializer, LibroSerializer, PrestamoSerializer

from rest_framework import viewsets

import datetime

# Create your views here.
def index(request):
    """ Vista para atender la petción de la url / """
    # Obteniendo los datos mediantes consultas
    prestamos = Prestamo.objects.all()
    grupos = request.user.groups.values_list("name", flat=True)

    return render(request, "catalogo/index.html",
        {"prestamos":prestamos, "grupos":grupos}
    )

@login_required()
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

@login_required()
def elimina_libros_prestamo(request, idPrestamo, idLibro):
    """
    Atiende la petición GET
       /prestamo/<int:idPrestamo>/libros/elimina/<int:idLibro>/
    """
    # Se valida que el usuario pertenesca al grupo eliminar
    grupos = request.user.groups.values_list("name", flat=True)
    if "eliminar" in grupos:
        # Se obtienen los objetos correspondientes a los id's
        prestamo = Prestamo.objects.get(pk=idPrestamo)
        libro = Libro.objects.get(pk=idLibro)

        # Se elimina el libro del préstamo
        prestamo.libros.remove(libro)

    return redirect("/")

# Vistas basadas en clases para Django Rest
class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones en la tabla Usuario
    """
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso sobre todos los usuarios disponibles.
    queryset = Usuario.objects.all().order_by('id')
    # Se define el Serializador encargado de transformar la peticiones
    # en formato JSON a objetos de Django y de Django a JSON.
    serializer_class = UsuarioSerializer


class LibroViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones en la tabla Libro
    """
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso sobre todos los libros disponibles.
    queryset = Libro.objects.all().order_by('id')
    # Se define el Serializador encargado de transformar la peticiones
    # en formato JSON a objetos de Django y de Django a JSON.
    serializer_class = LibroSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    """
    API que permite realizar operaciones en la tabla Prestamo
    """
    # Se define el conjunto de datos sobre el que va a operar la vista,
    # en este caso sobre todos los prestamos disponibles.
    queryset = Prestamo.objects.all().order_by('id')
    # Se define el Serializador encargado de transformar la peticiones
    # en formato JSON a objetos de Django y de Django a JSON.
    serializer_class = PrestamoSerializer
