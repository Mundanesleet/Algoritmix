from django.db import models

class Modulo(models.Model):
    numero = models.IntegerField(unique=True, default=1)  # Campo para el número del módulo, único
    nombre = models.CharField(max_length=100, default="Default Module Name")  # Nombre del módulo

    class Meta:
        ordering = ['numero']  # Asegura que los módulos se ordenen por el número

    def __str__(self):
        return f'Módulo {self.numero}: {self.nombre}'

class Leccion(models.Model):
    modulo = models.ForeignKey(Modulo, related_name='lecciones', on_delete=models.CASCADE)  # Relación con el módulo
    titulo = models.CharField(max_length=200)  # Título de la lección
    contenido = models.TextField()  # Contenido de la lección
    orden = models.IntegerField()  # Orden de la lección dentro del módulo

    class Meta:
        ordering = ['modulo__numero', 'orden']  # Asegura que las lecciones se ordenen primero por módulo y luego por orden

    def __str__(self):
        return f"{self.modulo.numero}/{self.orden}: {self.titulo}"
