def descuentos(precio: float) -> float:
    if precio < 100:
        descuento = 0.05
    elif precio <= 500:
        descuento = 0.10
    else:
        descuento = 0.15

    final_precio = precio - (precio * descuento)
    print(f"Precio original: {precio}€ - Descuento aplicado: {descuento * 100}% - Precio final: {final_precio}€")
    return final_precio


if __name__ == "__main__":
    descuentos(1000)