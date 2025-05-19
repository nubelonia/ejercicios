def nota(calificacion: int) -> str:
    # Delimitamos el rango de calificaciones
    
    if calificacion < 0 or calificacion > 100:
        print("Calificación no válida. Debe estar entre 0 y 100.")
        return None

    if calificacion >= 90:
        nivel = "A"
    elif calificacion >= 80:
        nivel = "B"
    elif calificacion >= 70:
        nivel = "C"
    elif calificacion >= 60:
        nivel = "D"
    else:
        nivel = "F"

    print(f"Calificación numérica: {calificacion} - Nivel de calificación obtenido (letra): {nivel}")
    return nivel


if __name__ == "__main__":
    # Solicitamos la calificación al usuario con el input
    
    intro_calificacion = int(input("Introduce la calificación (0-100): "))
    nota(intro_calificacion)
    
