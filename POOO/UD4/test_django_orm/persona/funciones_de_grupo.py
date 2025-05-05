import os
import django
import sys
from django.db.models import Avg, Count, Max, Min, Sum

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append('C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/test_django_orm')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_orm.settings')
django.setup()

from persona.models import Persona

# Funciones agregado
mayor_id = Persona.objects.aggregate(Max('id'))
menor_id = Persona.objects.aggregate(Min('id'))
contar = Persona.objects.filter(correo__contains='gmail').aggregate(Count('id'))
promedio = Persona.objects.aggregate(Avg('id'))

print(f'Mayor id: {mayor_id}')
print(f'Menor id: {menor_id}')
print(f'Contar: {contar}')
print(f'Promedio: {promedio}')