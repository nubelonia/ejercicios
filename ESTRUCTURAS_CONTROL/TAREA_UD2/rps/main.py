def run(player1: str, player2: str) -> int:
    # Para que reconozca las entradas en minúsculas, es necesario lower()
    p1 = player1.lower()
    p2 = player2.lower()

    print(f"Jugadora 1:  '{player1}'")
    print(f"Jugadora 2:  '{player2}'")

    if p1 == p2:
        print("Salida :  (empate)")
        return 0
    elif p1 == 'rock':
        if p2 == 'scissors':
            print("Salida :  (piedra vence a tijeras)")
            return 1
        elif p2 == 'paper':
            print("Salida :  (papel vence a piedra)")
            return 2
    elif p1 == 'paper':
        if p2 == 'rock':
            print("Salida :  (papel vence a piedra)")
            return 1
        elif p2 == 'scissors':
            print("Salida :  (tijeras vencen a papel)")
            return 2
    elif p1 == 'scissors':
        if p2 == 'paper':
            print("Salida :  (tijeras vencen a papel)")
            return 1
        elif p2 == 'rock':
            print("Salida :  (piedra vence a tijeras)")
            return 2

    # En caso de error (por si se introdujera otra palabra)
    print("Salida :  (entrada no válida)")
    return -1

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
