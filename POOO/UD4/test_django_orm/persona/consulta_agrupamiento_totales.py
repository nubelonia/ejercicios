import os
import django
import sys
# Agrega el directorio raíz del proyecto al sys.path
sys.path.append('C:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/test_django_orm')
from django.db.models import Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_django_orm.settings")
django.setup()

from persona.models import Persona

print("Agrupar y contar")

result = Persona.objects.values_list('nombre').annotate(total=Count('nombre'))

for tupla in result:
    print(tupla)