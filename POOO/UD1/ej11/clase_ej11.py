'''
Diseñar la clase “Empleado” con los atributos identificador, nombre, 
departamento, salario. Tener en cuenta que el salario será privado. 
Define un método para obtenerlo y otro para modificarlo. 
Programa el método eq(), de forma que indique si dos empleados 
son iguales o no en función de su salario.
Crear varios empleados, mostrar sus datos y comparar si son iguales o no.

'''
class Empleado:
    def __init__(self, id, nombre, departamento, salario):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento
        self.__salario = salario  # atributo privado

    # Método para obtener el salario
    def obtener_salario(self):
        return self.__salario

    # Método para modificar el salario
    def modificar_salario(self, nuevo_salario):
        self.__salario = nuevo_salario

    # Método para mostrar datos del empleado
    def mostrar_datos(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Departamento: {self.departamento}, Salario: {self.__salario}"
    
    # Para mostrar los datos, también podemos hacer uso del método dunder aprovechando
    # que ya tenemos el método mostrar_datos(), o sin el.
    def __str__(self):
        self.mostrar_datos()

    # Método especial para comparar empleados por salario
    def __eq__(self, otro):
        return self.__salario == otro.__salario
    

