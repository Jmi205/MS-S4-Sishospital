from django.db import models

class Diagnostico(models.Model):
    

    fechaDiagnostico = models.DateField()
    descripcion = models.CharField(max_length=255)
    recomendaciones = models.CharField(max_length=255)
    paciente = models.CharField(max_length=255)
    
    
    def __str__(self):
        return f"{self.paciente} - Fecha: {self.fechaDiagnostico}"


