'''
Programar una agenda de contactos. Definir la clase Contacto con los atributos 
nombre, teléfono y correo del contacto.
a. Añade el método str para que retorne todos los atributos con el formato:
Nombre – teléfono – correo.
b. Programa también repr para que retorne los datos del contacto con el formato: Contacto(nombre, teléfono, correo).
c. Programa el método eq para determinar si dos contactos son iguales.
En este caso serán iguales si coinciden todos los valores de sus atributos.

Programa la clase Agenda. Esta clase tendrá una lista de contactos 
y los métodos.

    - Buscar contacto por nombre y retornar el contacto.
    - Obtener el teléfono de un contacto. Retornar el teléfono.
    - Obtener el correo de un contacto. Retornar el correo.
    - Cambiar el teléfono de un contacto. Retornar True si se pudo hacer el cambio, 
    False en caso contrario.
    - Cambiar el correo de un contacto. Retornar True si se pudo hacer el cambio, False en caso contrario.
    - Listar todos los contactos.
    - Obtener el número de contactos.

'''

from clase_ej14 import *

# contacto_buscado = Agenda.buscar_contacto("Ana")
# print(contacto_buscado)

# nombre_contacto = "Anaddddddd"
# telefono = Agenda.telefono_de_contacto(nombre_contacto)
# if not telefono:   #ha devuelto None
#     print(f"No existe contacto {nombre_contacto}")
# else:
#     print(f"Teléfono de {nombre_contacto}: {telefono}")

#print(Agenda.correo_de_contacto("ana54545454"))

# Agenda.cambiar_telefono_contacto("Ana", "924000001")
# Agenda.cambiar_correo_contacto("Ana", "ana@movistar.com")

# contacto_buscado = Agenda.buscar_contacto("Ana")
# print(contacto_buscado)

Agenda.listar_contactos()

numero_contactos = Agenda.contar_contactos()
print(f"Nº de contactos en agenda: {numero_contactos}")

