from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para atender la petición GET / """
    return render(request, "reservas/index.html")
