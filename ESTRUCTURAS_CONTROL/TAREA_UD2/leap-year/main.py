def run(year: int) -> bool:
    # Hago uso de operadores lógicos para determinar si un año es bisiesto
    # Un año es bisiesto si es divisible por 4, pero no por 100, o bien que sea divisible
    # por 400
    # El operador % devuelve el resto de la división entre dos números
    # Por ejemplo, 2024 % 4 == 0, pero 2024 % 100 != 0    
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"El año {year} es bisiesto.")
        return True
    else:
        print(f"El año {year} no es bisiesto.")
        return False


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
