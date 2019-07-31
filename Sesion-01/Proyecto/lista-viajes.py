#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
# from modelomysql import ???
from stdout import imprime_registros, imprime_registros_html

@click.command()
@click.option("--html", is_flag=True, help="Imprime la lista en formato HTML")
def lista_viajes(html):
    """
    Imprime la lista de viajes resercados en la salida estándar
    """
    # Se obtiene la lista de viajes
    # viajes = ???
    pass

    # Si el usuario ha usado la opción --html entonces se imprime la
    # versión HTML, considera que en el módulo stdout hay una función
    # llamada imprime_registros_html() que puedes usar.
    pass

    # Si la opción --html no se ha usado entonces se imprime la versión
    # en sólo texto usando la función stdout.imprime_registros()
    pass


if __name__ == '__main__':
    lista_viajes()
