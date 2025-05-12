from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'lugar', 'descripcion')  # Campos que se mostrarán en la lista del admin
