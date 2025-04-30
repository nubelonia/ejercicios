'''
a. Sumar objetos Cadena. Se obtendrá un objeto str cuyo contenido será el
resultado de concatenar las cadenas de los objetos Cadena con los que se
opera.

'''

class Cadena:
    def __init__(self, texto):
        self.texto = texto

    # a. Sumar objetos Cadena.
    
    def __add__(self, otro):
        return self.texto + otro.texto
    

    '''
    b. Restar objetos Cadena. Al restar dos objetos Cadena, las vocales de la
segunda cadena se reemplazarán en la primera cadena por cadena vacía.
Por tanto, el primer objeto Cadena ve modificado el valor de su atributo.
Estudia el ejemplo:
    
    '''

    
    def __sub__(self, otro):
        vocales_a_eliminar = ""
        # El for con la variable "letra" recorre cada letra de la cadena2 = Cadena("tormenta")
        for letra in otro.texto:
            #Si es vocal y aún no está añadida, se agrega a la variable vacía vocales_a_eliminar
            if letra.lower() in "aeiou" and letra not in vocales_a_eliminar:
                vocales_a_eliminar += letra


        nuevo_texto = ""
        # El for recorre cada letra de la cadena1 = Cadena("El temor de un hombre sabio")
        for letra in self.texto:
            # Cada letra que no este en vocales_a_eliminar la añade a nuevo_texto
            if letra not in vocales_a_eliminar:
                nuevo_texto += letra
        # Reemplaza el texto original de la cadena1 por el nuevo_texto creado previamente
        self.texto = nuevo_texto
        return self.texto






    '''
    c. Longitud de un objeto Cadena. La longitud de una instancia de Cadena es
el número de vocales que tiene, incluidas mayúsculas y minúsculas con o
sin tilde.
    
    '''

    
    def __len__(self):
        # Defino una cadena que contenga todas las vocales, sean mayúsculas, minusculas con y sin tilde
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        # Creo la variable contador que empiece desde cero, para contar las vocales 
        contador = 0
        # El for recorre todas las letras del texto que se instancie en la clase Cadena
        for letra in self.texto:
            # Si en el recorrido encuentra letras como las que contiene vocales las suma al contador
            if letra in vocales:
                contador += 1
        return contador





    '''
    d. Compara objetos Cadena. Dos objetos Cadena son iguales si tienen la
misma longitud, es decir, el mismo número de vocales.
    
    '''
    # El método __eq__ permite comparar si la igualdad establecida es cierta o no
    def __eq__(self, otro):
        return len(self) == len(otro)




    '''
    e. Operador +=. Al realizar la operación cadena += valor_str, se añadirá al
atributo del objeto Cadena la cadena valor_str. El objeto original se verá
modificado.
    
    '''

    def __iadd__(self, otro):
        self.texto += otro
        return self
    



    #Este método es necesario para que pueda imprimir los strings de texto
    def __str__(self):
        return self.texto



