from modulo_gym import generar_json_actividad, generar_csv_filtrado

# Rutas absolutas reales de mi equipo
csv_entrada = "C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD3/Tarea3/ejercicio2/gym_data.csv"
salida_json = "C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD3/Tarea3/ejercicio2/actividades.json"
salida_csv = "C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD3/Tarea3/ejercicio2/filtro_female_HIIT.csv"

# Generar JSON
if generar_json_actividad(csv_entrada, salida_json):
    print("JSON generado correctamente.")
else:
    print("Error generando JSON.")

# Generar CSV filtrado
if generar_csv_filtrado(csv_entrada, salida_csv, "female", "HIIT"):
    print("CSV filtrado generado correctamente.")
else:
    print("Error generando CSV filtrado.")
