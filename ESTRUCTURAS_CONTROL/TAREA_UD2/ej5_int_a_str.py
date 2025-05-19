def num_a_texto(numero: int) -> str:
    match numero:
        case 1:
            print("Uno")
            return "Uno"
        case 2:
            print("Dos")
            return "Dos"
        case 3:
            print("Tres")
            return "Tres"
        case 4:
            print("Cuatro")
            return "Cuatro"
        case 5:
            print("Cinco")
            return "Cinco"
        case _:
            print("Número no válido. Introduce un número del 1 al 5.")
            return None


if __name__ == "__main__":
    numero = int(input("Introduce un número del 1 al 5: "))
    num_a_texto(numero)

