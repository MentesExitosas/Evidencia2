import numpy as np
import pandas as pd
import os
import sys
import datetime
import time

ventas = {}
precios_totales = []
menu = 1



while menu >= 1 and menu < 3:
    print("\n1. Registrar una venta\n2. Consultar ventas de un día específico\n3. Salir")
    menu = int(input("\n¿Qué opción desea elegir?\nOpción: "))

    try:
        if menu == 1:
            print("***REGISTRO DE VENTA***")
            cantidad = int(input("Cantidad de artículos que deseas registrar en la venta: "))
            for articulo in range (cantidad):
                descripcion = input("Escriba la descripción del artículo: ")
                cant_piezas = int(input("Número de piezas vendidas de este artículo: "))
                precio_venta = float(input("Precio de venta del artículo: $"))
                fecha_actual = datetime.date.today()
                ventas[descripcion] = cant_piezas,precio_venta,fecha_actual
                precios_totales.append((cant_piezas)*(precio_venta))
                total = sum(precios_totales)
            ventasdf = pd.DataFrame(ventas)
            ventasdf.index = ["Cantidad","Precio","Fecha"]
            print(ventasdf)
            print(f"\nEl total a pagar es: ${total}")
            precios_totales.clear()
            ventasdf.to_csv('historial.csv',mode = "a", index=True, header=True)
        if menu == 2:
            pedirfecha = int(input("¿Cuál es la fecha que quieres consultar? "))
            print("Fecha procesada")
            fecha_procesada = datetime.datetime.strptime(pedirfecha, "%Y-%m-%d").date()
            print(fecha_procesada)
            for elemento in ventas:
                if fecha_procesada in elemento:
                    print(elemento)
    except Exception:   
        print(f"Ocurrió un error {sys.exc_info()[0]}")


