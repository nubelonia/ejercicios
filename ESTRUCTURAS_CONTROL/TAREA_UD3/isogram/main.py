def run(text: str) -> bool:
    text = text.lower()
    letras_vistas = []

    for letra in text:
        if letra == '-':
            continue
        if letra in letras_vistas:
            # Si la letra ya ha sido vista, no es un isograma
            print(f"El texto {text} no es un isograma. Se repite la letra '{letra}'.")
            return False
        letras_vistas.append(letra)

    # Si no se han encontrado letras repetidas, es un isograma
    print(f"El texto {text} es un isograma.")    

    return True

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)