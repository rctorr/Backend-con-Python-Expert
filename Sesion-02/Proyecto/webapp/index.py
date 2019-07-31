#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, static_file, request

HOST = "localhost"
PORT = 8000

# Agregar ruta y vista para atender peticiones de archivos estáticos

# Agregar ruta y vista para atender petición raíz /

# Agregar ruta y vista para atender petición raíz / con datos POST


if __name__ == "__main__":
    # Inicializa el servidor de la aplicación web
    run(host=HOST, port=PORT, debug=True, reloader=True)
