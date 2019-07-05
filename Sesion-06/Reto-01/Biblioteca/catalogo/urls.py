from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("prestamo/nuevo/", views.nuevo_prestamo, name="nuevo_prestamo"),
    path("login/", views.login_user, name="login_user"),
]
