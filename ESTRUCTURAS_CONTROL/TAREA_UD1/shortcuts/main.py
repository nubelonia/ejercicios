def run(key1: str, key2: str, key3: str) -> str:
    match (key1, key2, key3):
        case ('CTRL', 'ALT', 'T'):
            accion = 'Open terminal'
        case ('CTRL', 'ALT', 'L'):
            accion = 'Lock screen'
        case ('CTRL', 'ALT', 'D'):
            accion = 'Show desktop'
        case ('ALT', 'F2', ''):
            accion = 'Run console'
        case ('CTRL', 'Q', ''):
            accion = 'Close window'
        case ('CTRL', 'ALT', 'DEL'):
            accion = 'Log out'
        # El guíon bajo _ es un comodín en match-case, y se ejecuta si 
        # no se cumple ninguno de los casos anteriores
        case _:
            accion = 'Undefined'

    print("Teclas pulsadas:", key1, key2, key3)
    print("Acción:", accion)

    return accion

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)

