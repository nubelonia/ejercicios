from clases import *

print("Ejecutando archivo de pruebas...")


# Partido de Fútbol

partido = Futbol("Málaga cf", "Granada", "25-04-25", "Liga", 2, 1)
print(partido.resultado())
print(partido.ganador())






# Partido de Baloncesto

partido = Baloncesto("Unicaja", "Cajasol", "25-04-25", "Liga ACB", 98, 89)
print(partido.resultado())
print(partido.ganador())




# Partido de Tenis

partido = Tenis("Nadal", "Federer", "2025-04-25", "Roland Garros", [6, 3, 6], [4, 6, 3])
print(partido.resultado())  # Muestra: "6-4, 3-6, 6-3"
print(partido.ganador())    # Muestra: "Nadal"

    
