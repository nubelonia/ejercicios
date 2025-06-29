import pandas as pd
import numpy as np
from pandas import json_normalize

print("EJERCICIO ENCUESTAS\n")

# EJERCICIO 2

# 1) IMPORTACIÓN Y EXPLORACIÓN INICIAL

# a) Importamos el archivo encuestas.json
df_json = pd.read_json("C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/ANALISIS_DINAMICO/tema2/tarea_tema2/encuestas.json")

# Usamos json_normalize para convertir la lista dentro de "datos" en columnas planas
df = json_normalize(df_json["datos"])

# b) Mostramos las últimas 5 filas del DataFrame
print("Últimas 5 filas del DataFrame:")
print(df.tail())

print("\n")

# 2) LIMPIEZA DE DATOS

# a) Eliminamos filas duplicadas según la columna 'Nombre'
df = df.drop_duplicates(subset=["Nombre"])

# b) Rellenamos valores nulos en 'Calificación_Curso' con la mediana
mediana_calif = df["Calificación_Curso"].median()
df["Calificación_Curso"] = df["Calificación_Curso"].fillna(mediana_calif)

print("DataFrame tras limpieza:")
print(df)

print("\n")

# 3) TRANSFORMACIÓN DE DATOS

# a) Discretizamos la Edad en tres categorías
def clasificar_edad(edad):
    if 18 <= edad <= 25:
        return "Joven"
    elif 26 <= edad <= 35:
        return "Adulto Joven"
    elif 36 <= edad <= 60:
        return "Adulto"
    else:
        return "Fuera de rango"

df["Categoria_Edad"] = df["Edad"].apply(clasificar_edad)

# b) Creamos columna 'Rendimiento' según Calificación_Curso
def clasificar_rendimiento(calif):
    if calif < 5:
        return "Bajo"
    elif 5 <= calif < 7:
        return "Medio"
    else:
        return "Alto"

df["Rendimiento"] = df["Calificación_Curso"].apply(clasificar_rendimiento)

print("DataFrame con categorías añadidas:")
print(df)

print("\n")

# 4) ANÁLISIS DE DATOS

# a) Promedio de Satisfacción por Carrera, ordenado de mayor a menor
promedio_satisfaccion = df.groupby("Carrera")["Satisfacción"].mean().sort_values(ascending=False)
print("Promedio de Satisfacción por Carrera (mayor a menor):")
print(promedio_satisfaccion)

print("\n")

# b) Filtramos estudiantes con Rendimiento 'Alto' y mostramos frecuencia de Satisfacción
rendimiento_alto = df[df["Rendimiento"] == "Alto"]
frecuencia_satisfaccion = rendimiento_alto["Satisfacción"].value_counts()
print("Frecuencia de Satisfacción entre estudiantes con Rendimiento 'Alto':")
print(frecuencia_satisfaccion)

print("\n")

