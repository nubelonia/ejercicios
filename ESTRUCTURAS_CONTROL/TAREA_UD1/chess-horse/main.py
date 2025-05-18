def run(target_x: int, target_y: int) -> int:
    # Caso especial: si ya estamos en el origen.
    if target_x == 0 and target_y == 0:
        print("Número de movimientos: 0")
        return 0

    # Verificamos si la suma de las coordenadas es divisible por 3.
    total = target_x + target_y
    if total % 3 != 0:
        print("La casilla de destino no se puede alcanzar.")
        return -1

    movimientos = total // 3

    # Verificamos que cada coordenada sea al menos igual al número de movimientos.
    if target_x < movimientos or target_y < movimientos:
        print("La casilla de destino no se puede alcanzar.")
        return -1

    print("Número de movimientos: " + str(movimientos))
    return movimientos


# NO TOCAR EL CÓDIGO DE ABAJO
if __name__ == '__main__':
    import vendor
    vendor.launch(run)
