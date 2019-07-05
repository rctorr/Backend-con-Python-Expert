from rest_framework import serializers

from .models import Usuario, Libro


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Usuario """
    class Meta:
        # Se define sobre que modelo actua
        model = Usuario
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'apellidos', 'edad', 'genero', 'direccion')


class LibroSerializer(serializers.HyperlinkedModelSerializer):
   """ Serializador para atender las conversiones para Libro """
   class Meta:
       # Se define sobre que modelo actua
       model = Libro
       # Se definen los campos a incluir
       fields = ('id', 'titulo', 'editorial', 'numPag', 'autores')
