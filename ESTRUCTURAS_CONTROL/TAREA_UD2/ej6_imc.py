def calcular_imc(peso: float, altura: float) -> float:
    imc = peso / (altura ** 2)
    # El .2f es para redondear a 2 decimales
    print(f"Tu IMC es: {imc:.2f}")

    match imc:
        case imc if imc < 16.00:
            print("Clasificación: Infrapeso - Delgadez Severa")
        case imc if 16.00 <= imc <= 16.99:
            print("Clasificación: Infrapeso - Delgadez Moderada")
        case imc if 17.00 <= imc <= 18.49:
            print("Clasificación: Infrapeso - Delgadez Aceptable")
        case imc if 18.50 <= imc <= 24.99:
            print("Clasificación: Peso Normal")
        case imc if 25.00 <= imc <= 29.99:
            print("Clasificación: Sobrepeso")
        case imc if 30.00 <= imc <= 34.99:
            print("Clasificación: Obeso - Tipo I")
        case imc if 35.00 <= imc <= 40.00:
            print("Clasificación: Obeso - Tipo II")
        case _:
            print("Clasificación: Obeso - Tipo III")
    
    return imc

if __name__ == "__main__":
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))
    calcular_imc(peso, altura)
