from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para atender la petición GET / """
    return HttpResponse("<h2>Son la página de inicio! Soñaré con BeduTravels!")
