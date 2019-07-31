#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
# Se requiere de una función que ejecute sql en el módulo modelomysql
# from modelomysql import ???  

# Posiblemente necesitemos una función extra

@click.command()
@click.argument("archsql", type=click.Path(exists=True))
def sql2mysql(archsql):
    """
    Ejecuta las instrucciones del archivo ARCHSQL en el servidor MariaDB
    """
    # Se obtiene el contenido del archivo archsql y guardarlo en la
    # variable sql.
    pass

    # Ejecutar las instruciones en la variable sql
    pass

    # Si el resultado es True mostrar mensaje de éxito
    pass

    # Si el resultado es False no mostrar nada o un mensaje de error
    pass

if __name__ == '__main__':
    sql2mysql()
