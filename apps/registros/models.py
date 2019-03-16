from django.db import models
from django.utils import timezone

class ticket(models.Model):

    ## Tupla con opciones para el campo estado
    opciones_estado = (
        ('A', 'Abierto'),
        ('P', 'Pendiente'),
        ('E', 'En Proceso'),
        ('C', 'Cerrado'),
    )

    titulo = models.CharField(max_length=250, null=False, verbose_name="Título")
    descripcion = models.CharField(max_length=250, null=False, verbose_name="Descripción")
    estado = models.CharField(max_length=1, choices=opciones_estado, blank=True)
    fecha_creacion = models.DateField(default=timezone.now)