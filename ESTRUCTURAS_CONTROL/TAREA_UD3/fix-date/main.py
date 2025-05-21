def run(input_date: str, base_year: int) -> str:
    mes, dia, anio_2dig = input_date.split('/')
    
    # Convertimos a int y sumamos al año base
    anio_completo = base_year + int(anio_2dig)

    # Aseguramos que día y mes tengan 2 dígitos
    if len(dia) == 1:
        dia = '0' + dia
    if len(mes) == 1:
        mes = '0' + mes

    resultado = f"{dia}-{mes}-{anio_completo}"
    print(f"Fecha transformada: {resultado}")  
    return resultado


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
