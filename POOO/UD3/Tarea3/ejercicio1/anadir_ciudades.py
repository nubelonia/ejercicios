import os

def añadir_ciudades(archivo_destino, archivo_fuente):
    """
    Añade el contenido de archivo_fuente al final de archivo_destino.
    Ambos deben ser rutas absolutas.
    Retorna True si la operación se realiza con éxito, False si hay error.
    """
    try:
        # Verifica que ambos archivos existan
        if not os.path.isabs(archivo_destino) or not os.path.isabs(archivo_fuente):
            print("Las rutas deben ser absolutas.")
            return False

        if not os.path.exists(archivo_destino):
            print(f"El archivo destino no existe: {archivo_destino}")
            return False

        if not os.path.exists(archivo_fuente):
            print(f"El archivo fuente no existe: {archivo_fuente}")
            return False

        # Abrimos el archivo fuente para lectura y el destino para añadir (append)
        with open(archivo_fuente, 'r', encoding='utf-8') as fuente, \
             open(archivo_destino, 'a', encoding='utf-8') as destino:
            for linea in fuente:
                destino.write(linea)
        
        return True
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False
