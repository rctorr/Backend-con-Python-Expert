from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers

from . import views

# Agregando rutas para django rest
router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'prestamos', views.PrestamoViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("prestamo/nuevo/", views.nuevo_prestamo, name="nuevo_prestamo"),
    path("prestamo/<int:idPrestamo>/libros/elimina/<int:idLibro>/",
        views.elimina_libros_prestamo, name="elimina_libros_prestamo"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),

    # Rutas para la url /api/
    path("api/", include(router.urls)),
    # Rutas para la autenticación url /api/auth/
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
]
