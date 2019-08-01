from django.db import models

# Create your models here.
class Usuario(models.Model):
    """ Define la tabla Usuario """
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=80)
    edad = models.SmallIntegerField()
    GENERO_OPCIONES = [
        ("M", "Mujer"),
        ("H", "Hombre"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_OPCIONES)
    direccion = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        """ Se define la representación en str para Usuario """
        return "{} {}".format(self.nombre, self.apellidos)


class Libro(models.Model):
    """ Define la tabla Libro """
    titulo = models.CharField(max_length=128)
    editorial = models.CharField(max_length=80)
    numPag = models.SmallIntegerField()
    autores = models.SmallIntegerField()

    def __str__(self):
        """ Se define la representación en str para Libro """
        return self.titulo


class Prestamo(models.Model):
    """ Define la tabla Prestamo """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="prestamos")
    fechaPre = models.DateField(auto_now_add=True)
    fechaDev = models.DateField(null=True, blank=True)
    libros = models.ManyToManyField(Libro, related_name="prestamos")

    def __str__(self):
        """ Se define la representación en str para Prestamo """
        return str(self.id)
