import os
import sys
import django

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append('C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/test_django_orm')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_orm.settings')
django.setup()

from persona.models import Persona

# Buscar por id
persona = Persona.objects.get(id=1)
print(persona)