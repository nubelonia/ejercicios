def run(key1: str, key2: str, key3: str) -> str:
    # TODO      
    if key1 == 'CTRL':
        if key2 == 'ALT':
            if key3 == 'T':
                accion = 'Open terminal'
            elif key3 == 'L':
                accion = 'Lock screen'
            elif key3 == 'D':
                accion = 'Show desktop'
            elif key3 == 'DEL':
                accion = 'Log out'
            else:
                accion = 'Undefined'
        elif key2 == 'Q' and key3 == '':
            accion = 'Close window'
        else:
            accion = 'Undefined'
    elif key1 == 'ALT' and key2 == 'F2' and key3 == '':
        accion = 'Run console'
    else:
        accion = 'Undefined'

    print(f"Teclas pulsadas: {key1}, {key2}, {key3}")  
    print(f"Acción: {accion}")
    return accion

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
