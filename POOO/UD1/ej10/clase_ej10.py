'''
Diseñar una clase llamada “Mates” con los métodos estáticos que se describen:
a. mayor. Recibe dos números como argumento y retorna el mayor.
b. producto. Recibe tres números como argumento y retorna su producto.
c. potencia. Recibe una base y un exponente como argumentos y retorna la base elevada al exponente.
Probar los métodos programados.
'''

class Mates():
    
    @staticmethod
    def mayor(x, y):
        if x > y:
            return x
        else:
            return y
        
    @staticmethod
    def producto(x, y ,z):
        return x*y*z
    
    
    @staticmethod
    def potencia(base, exponente):
        return base ** exponente



