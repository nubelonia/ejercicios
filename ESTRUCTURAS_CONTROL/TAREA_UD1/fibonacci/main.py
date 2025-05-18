def run(n: int) -> int:
    # • Siempre se cumple que el primer valor de la sucesión de Fibonacci es el cero y el
    # segundo valor es el uno.

    if n == 0: # Si n es 0, el primer 0 de la sucesión de Fibonacci
        print("El número en la posición 0 de la sucesión de Fibonacci es 0")
        return 0
    if n == 1: # Si n es 1, el segundo 1 de la sucesión de Fibonacci
        print("El número en la posición 1 de la sucesión de Fibonacci es 1")
        return 1

    # • A partir de ahí, cada nuevo valor se calcula como la suma de los dos valores anteriores.

    # a y b guardan los dos últimos números de la sucesión
    a = 0
    b = 1

    for _ in range(2, n + 1):
        # temp guarda el siguiente numero, que es la suma de los dos anteriores
        temp = a + b
        a = b
        b = temp

    print(f"El número en la posición {n} de la sucesión de Fibonacci es {b}")
    return b



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
