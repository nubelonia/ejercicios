def run(limit: int) -> None:
    suma = 0
    numero = 0
    resultado = None  # Comenzamos sin una cadena vacía

    while suma < limit:
        if resultado is None:
            # En la primera iteración, convertimos el primer número a cadena.
            resultado = str(numero)
        else:
            # En las siguientes iteraciones, se añade un espacio y el número convertido.
            resultado = resultado + " " + str(numero)
        suma = suma + numero
        numero = numero + 3

    print(resultado)

   
    
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)


