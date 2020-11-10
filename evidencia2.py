import numpy as np
import pandas as pd

diccionario_ventas = {}

print("1. Registrar una venta\n 2. Consultar ventas de un día específico\n 3. Salir")
menu = int(input("¿Qué opción desea elegir?"))

try:
    if menu == 1:
        print("***REGISTRO DE VENTA***")
        cantidad = int(input("¿Cuántos artículos deseas registrar en la venta?"))
        for articulo in range (cantidad):
            descripcion = input("Escriba la descripción del artículo:\n")
            cant_piezas = int(input("¿Cuántas piezas vendió de este artículo?"))
            precio_venta = int(input("¿Cuál fue el precio de venta del artículo"))
    