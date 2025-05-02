from anadir_ciudades import *
import os

# Obtener la ruta absoluta desde la ubicación del script
base = os.path.dirname(os.path.abspath(__file__))
ruta_destino = os.path.join(base, "ciudades.csv")
ruta_fuente = os.path.join(base, "mas_ciudades.csv")

# Verificamos si son absolutas (opcional para depurar)
print("Destino absoluto:", os.path.isabs(ruta_destino))
print("Fuente absoluta:", os.path.isabs(ruta_fuente))

resultado = añadir_ciudades(ruta_destino, ruta_fuente)

if resultado:
    print("Contenido añadido correctamente.")
else:
    print("No se pudo completar la operación.")

