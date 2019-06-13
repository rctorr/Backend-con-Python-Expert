#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Leer la imagen desde el archivo "img/python-logo.png" en modo binario y
# guardarlo en la varible imagen.
pass

# Se envía la imagen y el encabezado en modo binario a la salida estándar.
# 1 es el descriptor de archivo a nivel S.O. para la salida estándar.
os.write(1, b"Content-Type: image/png\n\n")
os.write(1,imagen)
