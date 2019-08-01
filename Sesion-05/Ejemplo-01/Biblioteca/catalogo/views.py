from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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

def login_user(request):
    """ Atiende las peticiones de GET /login/ """

    # Si hay datos vía POST se procesan
    if request.method == "POST":
        # Se obtienen los datos del formulario
        username = request.POST["username"]
        password = request.POST["password"]
        next = request.GET.get("next", "/")
        acceso = authenticate(username=username, password=password)
        if acceso is not None:
            # Se agregan datos al request para mantener activa la sesión
            login(request, acceso)
            # Y redireccionamos a next
            return redirect(next)
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST
        msg = ""

    return render(request, "registration/login.html",
        {
            "msg":msg,
        }
    )
