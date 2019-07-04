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
