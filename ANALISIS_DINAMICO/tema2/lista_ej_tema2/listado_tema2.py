'''
Datos para la Serie:
4, 7, -5, 3 y asigna los índices 'a', 'b', 'c', 'd'
Datos para el DataFrame:
'''

import pandas as pd
import numpy as np

print("EJERCICIO 1\n")
ejer1_serie = pd.Series([4, 7, -5, 3], index=["a", "b", "c", "d"])
print(ejer1_serie)

datos = {'A':[1.5, 3.3, 2.4, 10.0],
         'B':["Gallina", "Pollo", "Vaca", "Burro"],
         'C':[10, 20, 30, 40],
         'D':[True, False, False, True]}

ejer1_df = pd.DataFrame(datos)
print(ejer1_df)

###########

'''
1) Muestra el número de elementos de la serie.
2) Consulta si hay valores faltantes en la serie.
3) Selecciona el valor correspondiente al índice 'b'.
4) Filtra los valores mayores que 0.
'''
print("\n")
print("EJERCICIO 2\n")
ejer1_serie = pd.Series([4, 7, -5, 3], index=["a", "b", "c", "d"])
print(ejer1_serie)

# Muestra el número de elementos de la serie
print(ejer1_serie.size)

# Consulta si hay valores faltantes en la serie
print(pd.isna(ejer1_serie))

# Selecciona el valor correspondiente al índice 'b'
print(ejer1_serie["b"])

# Filtra los valores mayores que 0
mayor_que_cero = ejer1_serie[ejer1_serie > 0]
print(mayor_que_cero)

print("\n")

'''
1) Muestra la columna 'B'.
2) Muestra la primera fila del DataFrame.
3) Añade una columna nueva llamada ‘Extra’
4) Muestra el DataFrame traspuesto
5) Inserte valores a la nueva columna ‘Extra’
'''
print("EJERCICIO 3\n")

datos = {'A':[1.5, 3.3, 2.4, 10.0],
        'B':["Gallina", "Pollo", "Vaca", "Burro"],
        'C':[10, 20, 30, 40],
        'D':[True, False, False, True]}

ejer1_df = pd.DataFrame(datos)

print(ejer1_df)

# Muestra la columna 'B'.
print(ejer1_df['B'])

# Muestra la primera fila del DataFrame.
print(ejer1_df.iloc[0])

# Añade una columna nueva llamada 'Extra'
ejer1_df = pd.DataFrame(datos, columns=['A', 'B', 'C', 'D', 'Extra'])
print(ejer1_df)

# Muestra el DataFrame traspuesto
print(ejer1_df.T)

# Inserte valores a la nueva columna 'Extra'
ejer1_df['Extra'] = 1
print(ejer1_df)

#############
print("\n")

'''
Crea dos Series s1 y s2
Valores para s1: 1, 2, 3, 4
Valores para s2: 4, 3, 2, 1.
Realiza las operaciones de suma, resta,
multiplicación y división entre ambas Series.
'''
print("EJERCICIO 4\n")

s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([4, 3, 2, 1])

# Suma
print(s1 + s2)

# Resta
print(s1 - s2)

# Multiplicación
print(s1 * s2)

# División
print(s1 / s2)

###########
print("\n")

'''
Crea este DataFrame
Identifica los valores nulos y reemplázalos por el
valor 0.
Exporta el resultado en formato html con el
nombre “ejer5_sin_nulos.html”
'''
print("EJERCICIO 5\n")

ejer5 = pd.DataFrame({'A':[1.0, np.nan, 3.0],
                      'B':[4.0, 5.0, np.nan],
                      'C':[np.nan, 8.0, 9.0]})

print(ejer5.isna())

ejer5 = ejer5.fillna(0)
print(ejer5)

ejer5.to_html("ejer5_sin_nulos.html")

###########
print("\n")

'''
Con el DataFrame del ejercicio anterior
Calcula las medias, desviaciones estándar y el
resumen estadístico general de cada columna.
'''

print("EJERCICIO 6\n")

ejer5 = pd.DataFrame({'A':[1.0, np.nan, 3.0],
                      'B':[4.0, 5.0, np.nan],
                      'C':[np.nan, 8.0, 9.0]})

ejer5 = ejer5.fillna(0)

# Media
print(ejer5.mean())

# Desviaciones estándar
print(ejer5.std())

# Resumen estadístico general
print(ejer5.describe())

###########
print("\n")

'''
Con el DataFrame siguiente
1. Ordena en orden ascendente según la
columna ‘A’ y luego en orden descendente
según la columna 'B'.
2. Cambia el índice de las filas por ‘Plata’,
‘Oro’, ‘Cobre’ y ‘Platino’ y ordena por el
nombre de las filas.
'''

print("EJERCICIO 7\n")

import pandas as pd

ejer7 = pd.DataFrame({'A':[3, 1, 2, 7],
                     'B':[1, 5, 8, 0],
                     'C':[4, 9, 6, 10]})

# Orden ascendente
ejer7.sort_values('A')

# Orden descendente
ejer7.sort_values('B',ascending=False)

# Ordenar por el índice de filas
ejer7.index=["Plata", "Oro", "Cobre", "Platino"]
ejer7.sort_index()
print(ejer7)

##########
print("\n")



'''
Lee el fichero empleados.csv
1. Muestra el número de identificación de aquellos
empleados que cobran más de 9000€ y que su
departamento sea Ventas (30)
2. Incrementa el sueldo de todos un 10%
3. Determina qué valores de sueldo son atípicos
4. Detecta duplicados y elimínalos en caso de haberlos
5. Añade una función que clasifique los empleados por el
ID de su departamento: Ventas (30), RRHH (40),
Investigación (20), Administración (10), Logística (50),
Finanzas (100), Otro.
'''

print("EJERCICIO 8\n")

# Codificación latin-1 para poder trabajar con caracteres especiales
ejer8 = pd.read_csv("C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/ANALISIS_DINAMICO/tema2/lista_ej_tema2/empleados.csv", encoding='latin1')
print(ejer8)

# Filtramos empleados de Ventas con sueldo superior a 9000€
apartado1 = ejer8[(ejer8["sueldo"] > 9000) & (ejer8["ID_departamento"] == 30)]
print(apartado1)

# Incrementamos sueldos un 10%
ejer8["sueldo"] = ejer8["sueldo"] * 1.10
print(ejer8)

# Detectamos valores atípicos
Q1 = ejer8["sueldo"].quantile(0.25)
Q3 = ejer8["sueldo"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = ejer8[(ejer8["sueldo"] < limite_inferior) | (ejer8["sueldo"] > limite_superior)]
print(outliers)

# Detecta duplicados y elimina si los hay
apartado4 = ejer8.duplicated()

if apartado4.any():
    print("Hay duplicados")
    ejer8.drop_duplicates()
else:
    print("No hay duplicados")

# Crea función para determinar el departamento de cada empleado
clave_departamento = {
    30: "Ventas",
    40: "RRHH",
    20: "Investigación",
    10: "Administración",
    50: "Logística",
    100: "Finanzas"
}

def get_departamento(n):
    return clave_departamento.get(n, "Otro")

ejer8["Departamento"] = ejer8["ID_departamento"].map(get_departamento)
print(ejer8)

#########

print("\n")

'''
Partiendo de este trozo de código:
1. Sustituye el nombre de las columnas por estos nuevos valores
valores = [“Animales”, “Clase”, “Grupo”, “Tipos”, “Fecha_consulta”]
2. Agrupa por Grupo y muestra la cantidad de animales que hay en cada
uno.
3. Cambia la fecha de consulta a tipo datetime y obtén todos los
consultados antes de 2020
'''

print("EJERCICIO 9\n")

animales = pd.DataFrame({
    "A": ["Saltamontes", "Cerdo", "Lubina", "Caballo", "Ciempiés"],
    "B": ["Insecto", "Mamífero", "Pez", "Mamífero", "Miriápodo"],
    "C": ["Invertebrado", "Vertebrado", "Vertebrado", "Vertebrado", "Invertebrado"],
    "D": [17, 100, 12, 200, 3300],
    "E": ["2020-01-15", "2019-02-20", "2020-06-10", "2018-09-30", "2021-01-01"]
})

# Cambiamos columnas
valores = ["Animales", "Clase", "Grupo", "Tipos", "Fecha_consulta"]
animales.columns = valores
print(animales)

# Agrupamos por grupos y contamos animales
animales_por_grupos = animales.groupby("Grupo")["Animales"].count()
print(animales_por_grupos)

# Cambiamos a tipo datetime y filtramos los anteriores a 2020
animales["Fecha_consulta"] = pd.to_datetime(animales["Fecha_consulta"])
print(animales[animales["Fecha_consulta"].dt.year < 2020])

###########

print("\n")

'''
Partiendo de este trozo de código:
1. Crea una columna llamada "Categoría_Precio" que clasifique los
productos en:
"Económico": Precio < 300
"Intermedio": 300 ≤ Precio < 800
"Premium": Precio ≥ 800
2. Crea una columna llamada "Velocidad_Venta" que categorice las
ventas según las horas de publicación:
"Rápido": Si se vendieron ≥100 unidades en ≤2 horas.
"Normal": Si no cumple lo anterior pero vendió ≥50 unidades en ≤5 horas.
"Lento": En cualquier otro caso.
'''

print("EJERCICIO 10\n")

data = {
    "producto": ["Laptop X1", "Smartphone A9", "Tablet Z3", "Monitor G5", "Teclado M2"],
    "precio": [1200, 600, 350, 250, 50],
    "cantidad_vendida": [45, 120, 80, 30, 200],
    "horas_publicacion": [3, 1, 5, 8, 2]
}

df = pd.DataFrame(data)

# Discretización precios
grupos_precio = [0, 300, 800, float('inf')]
etiquetas_precio = ["Económico", "Intermedio", "Premium"]
df["Categoria_Precio"] = pd.cut(df["precio"], bins=grupos_precio, labels=etiquetas_precio)

# Clasificación de velocidad de venta
def clasificar_venta(fila):
    if fila["cantidad_vendida"] >= 100 and fila["horas_publicacion"] <= 2:
        return "Rápido"
    elif fila["cantidad_vendida"] >= 50 and fila["horas_publicacion"] <= 5:
        return "Normal"
    return "Lento"

df["Velocidad_Venta"] = df.apply(clasificar_venta, axis=1)

print(df)







