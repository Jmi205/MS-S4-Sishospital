from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    tipoSangre = models.CharField(max_length=200)
    alergias= models.CharField(max_length=200)
    condicionesMedicas = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    historiaClinica = models.CharField(max_length=200)

    def __str__ (self):
        return self.apellido + " "  + self.nombre


