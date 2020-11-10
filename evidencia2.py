import numpy as np
import pandas as pd
import os
import sys
import time

diccionario_ventas = {}
menu = 1

while menu >= 1 and menu < 3:
    print("\n1. Registrar una venta\n2. Consultar ventas de un día específico\n3. Salir")
    menu = int(input("\n¿Qué opción desea elegir?\nOpción: "))

    try:
        if menu == 1:
            print("***REGISTRO DE VENTA***")
            cantidad = int(input("¿Cuántos artículos deseas registrar en la venta?"))
            for articulo in range (cantidad):
                descripcion = input("Escriba la descripción del artículo:\n")
                cant_piezas = int(input("¿Cuántas piezas vendió de este artículo?"))
                precio_venta = int(input("¿Cuál fue el precio de venta del artículo"))
            print("LISTO")

    except Exception:   
        print(f"Ocurrió un error {sys.exc_info()[0]}")


