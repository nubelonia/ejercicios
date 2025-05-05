import os
import django
import sys


# Agrega el directorio raíz del proyecto al sys.path
sys.path.append('C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/test_django_orm')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_orm.settings')
django.setup()

from persona.models import Persona

# Filtrar por nombre con OR
personas = Persona.objects.filter(nombre='Juan') | Persona.objects.filter(nombre='Ana')

for persona in personas:
    print(persona)