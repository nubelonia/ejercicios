def run(target_number: int) -> None:
    intentos = 0
    acierto = False

    while not acierto:
        intento = int(input("Introduzca número: "))
        intentos += 1

        if intento < target_number:
            print("Mayor")
        if intento > target_number:
            print("Menor")
        if intento == target_number:
            print(f"Enhorabuena has encontrado el número en {intentos} intentos")
            acierto = True

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
