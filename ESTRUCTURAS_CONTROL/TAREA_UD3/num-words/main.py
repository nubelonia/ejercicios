def run(text: str) -> int:
    # TODO
    # Contar el numero de palabras en el texto
    numero_de_palabras = 0
    palabras = text.split()
    for palabra in palabras:
        if palabra != '':
            numero_de_palabras += 1
    print(f"El texto '{text}' tiene {numero_de_palabras} palabras")
    return numero_de_palabras
    


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
