def run(x1: int, x2: int) -> tuple:
    # TODO
    # Definimos la función f(x)
    def f(x):
        return x * x - 6 * x + 3

    # Inicializamos el mínimo provisional en x1
    min_x = x1
    min_fx = f(x1)

    # Recorremos todos los valores de x en el intervalo cerrado [x1, x2]
    for x in range(x1, x2 + 1):
        valor = f(x)

        # Si el nuevo valor es menor que el mínimo actual, lo actualizamos
        if valor < min_fx:
            min_fx = valor
            min_x = x
        # Si no, no hacemos nada

    # Mostramos el resultado
    print(f"El valor mínimo se alcanza en x = {min_x}")
    print(f"donde f(x) = {min_fx}")

    return min_x, min_fx


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
