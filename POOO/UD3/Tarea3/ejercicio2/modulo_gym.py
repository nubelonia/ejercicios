import csv
import json
from collections import defaultdict

def generar_json_actividad(input_csv, output_json):
    """
    Genera un archivo JSON con las parejas nombre-actividad: [total, mujeres, hombres]
    """
    try:
        actividad_data = defaultdict(lambda: [0, 0, 0])  # [total, mujeres, hombres]

        with open(input_csv, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # saltar cabecera

            for fila in reader:
                genero = fila[1].strip().lower()
                actividad = fila[8].strip()

                actividad_data[actividad][0] += 1
                if genero == "female":
                    actividad_data[actividad][1] += 1
                elif genero == "male":
                    actividad_data[actividad][2] += 1

        with open(output_json, 'w', encoding='utf-8') as f_out:
            json.dump(actividad_data, f_out, indent=4)

        return True

    except Exception as e:
        print(f"Error al generar JSON: {e}")
        return False


def generar_csv_filtrado(input_csv, output_csv, genero_filtro, actividad_filtro):
    """
    Genera un archivo CSV con las columnas Age, Gender, Hours, Activity
    filtrando por género y actividad.
    """
    try:
        with open(input_csv, newline='', encoding='utf-8') as f_in, \
             open(output_csv, 'w', newline='', encoding='utf-8') as f_out:

            reader = csv.reader(f_in)
            writer = csv.writer(f_out)

            next(reader)  # saltar cabecera
            writer.writerow(["Age", "Gender", "Hours", "Activity"])  # cabecera de salida

            for fila in reader:
                genero = fila[1].strip().lower()
                actividad = fila[8].strip()

                if genero == genero_filtro.lower() and actividad.lower() == actividad_filtro.lower():
                    edad = fila[0].strip()
                    horas = fila[6].strip()
                    writer.writerow([edad, genero.capitalize(), horas, actividad])

        return True

    except Exception as e:
        print(f"Error al generar CSV filtrado: {e}")
        return False
