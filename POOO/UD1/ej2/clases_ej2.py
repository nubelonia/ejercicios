'''
2. En este ejercicio utilizaremos la misma clase que en el ejercicio anterior y
añadiremos un método llamado “nombre_completo” que retorne en una cadena los
atributos marca y modelo concatenados y separados por un guión (Seat-Ibiza).
Crear dos objetos y probar el método.

'''
class Vehiculo:

    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    #Creamos el metodo nombre_completo str, para que devuelva concatenado la marca y el modelo 

    def nombre_completo(self):
        return f"{self.marca} - {self.modelo}"
    
'''
Ojo!! Otra alternativa es asi, aunque según fuentes consultadas, el de arriba, es más limpio, eficiente (al evitar concatenación manual
por cada signo "+", y menos propenso a errores)

def nombre_completo(self):
    return self.marca + "-" + self.modelo
    
'''