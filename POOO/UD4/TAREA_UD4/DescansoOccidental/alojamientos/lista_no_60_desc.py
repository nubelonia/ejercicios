import os
import sys
import django

# Agregar la ruta del proyecto al sistema
sys.path.append("c:/Users/goku/Desktop/CE_PYTHON/POOO/ejercicios/POOO/UD4/TAREA_UD4/DescansoOccidental")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DescansoOccidental.settings')
django.setup()

from alojamientos.models import Hotel

# Filtrar por año con exclude
hoteles = Hotel.objects.exclude(ano_creacion='1960') and Hotel.objects.all().order_by('ano_creacion')

for hotel in hoteles:
    print(hotel)