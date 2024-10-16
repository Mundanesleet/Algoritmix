from django.contrib import admin
from .models import Modulo, Leccion

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nombre')  # Mostrar el número y nombre en la lista
    ordering = ('numero',)  # Asegurarse de que se ordenen por número

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('modulo', 'orden', 'titulo')  # Mostrar el módulo, orden y título en la lista
    ordering = ('modulo__numero', 'orden')  # Ordenar primero por módulo y luego por el orden
