import pandas as pd
import numpy as np

# EJERCICIO 1

# 1. IMPORTACIÓN Y EXPLORACIÓN INICIAL

# a. Importamos el archivo ventas.csv
ventas = pd.read_csv("C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/ANALISIS_DINAMICO/tema2/tarea_tema2/ventas.csv", encoding='latin1')  

# b. Mostramos las primeras 5 filas del DataFrame
print("Primeras 5 filas del DataFrame:")
print(ventas.head())

# c. Verificamos si hay valores nulos y mostramos el número por columna
print("\nNúmero de valores nulos por columna:")
print(ventas.isna().sum())


# 2. LIMPIEZA DE DATOS

# a. Eliminamos filas donde la columna 'Ciudad' sea nula
ventas = ventas.dropna(subset=["Ciudad"])

# b. Rellenamos valores nulos en la columna 'Descuento' con 0
ventas["Descuento"] = ventas["Descuento"].fillna(0)

# c. Reemplazamos valores negativos en 'Cantidad' y 'Total' por sus valores absolutos
ventas["Cantidad"] = ventas["Cantidad"].abs()
ventas["Total"] = ventas["Total"].abs()


# 3. TRANSFORMACIÓN DE DATOS

# a. Creamos la columna 'Precio_Final' calculando el descuento
ventas["Precio_Final"] = ventas["Total"] * (1 - ventas["Descuento"])

# b. Convertimos la columna 'Fecha' al tipo datetime
ventas["Fecha"] = pd.to_datetime(ventas["Fecha"], errors='coerce')


# 4. ANÁLISIS DE DATOS

# a. Filtramos ventas realizadas en Madrid y mostramos el promedio de Precio_Final
madrid_ventas = ventas[ventas["Ciudad"] == "Madrid"]
promedio_madrid = madrid_ventas["Precio_Final"].mean()
print(f"\nPromedio de Precio_Final para ventas en Madrid: {promedio_madrid:.2f}")

# b. Agrupamos por 'Producto' y mostramos la suma total de 'Cantidad' vendida
cantidad_por_producto = ventas.groupby("Producto")["Cantidad"].sum()
print("\nCantidad total vendida por producto:")
print(cantidad_por_producto)

# c. Identificamos filas donde el 'Total' sea un valor atípico usando rango intercuartílico
Q1 = ventas["Total"].quantile(0.25)
Q3 = ventas["Total"].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_total = ventas[(ventas["Total"] < limite_inferior) | (ventas["Total"] > limite_superior)]
print("\nFilas con valores atípicos en 'Total':")
print(outliers_total)


# 5. EXPORTACIÓN DE RESULTADOS

# Guardamos el DataFrame limpio y transformado en un nuevo CSV
ventas.to_csv("ventas_limpias_Manuel_Benitez.csv", index=False)
print("\nArchivo 'ventas_limpias_Manuel_Benitez.csv' guardado correctamente.")
