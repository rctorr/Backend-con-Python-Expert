from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para atender la petción de la url / """
    return render(request, "catalogo/index.html")
