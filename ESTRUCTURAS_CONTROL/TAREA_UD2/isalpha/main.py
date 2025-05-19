def run(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for letra in text:
        # Comprobamos si el carácter no está en el alfabeto permitido
        if letra not in ALPHABET:
            print(f"'{text}' → No es alfabética")
            return False

    print(f"'{text}' → Sí es alfabética")
    return True


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
