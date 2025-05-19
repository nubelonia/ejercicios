def run(num1: int, num2: int, op: str) -> float:
    match op:
        case '+':
            resultado = num1 + num2
        case '-':
            resultado = num1 - num2
        case '*':
            resultado = num1 * num2
        case '/':
            # Para evitar división por cero
            resultado = num1 / num2 if num2 != 0 else None
        case _:
            resultado = None

    print(f"Operación: {num1} {op} {num2} = {resultado}")
    return resultado


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
