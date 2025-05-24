from django.db import models

class Eventomedico(models.Model):
    CONSULTA = 1
    CIRUGIA = 2
    PRESCRIPCION = 3
    EXAMEN = 4

    TIPO_EVENTO_CHOICES = (
        (CONSULTA, "Consulta Médica"),
        (CIRUGIA, "Cirugía"),
        (PRESCRIPCION, "Prescripción de Medicamento"),
        (EXAMEN, "Examen"),
    )

    fechaEvento = models.DateField()
    descripcion = models.CharField(max_length=255)
    paciente = models.CharField(max_length=255)
    tipoEvento = models.IntegerField(
        choices=TIPO_EVENTO_CHOICES,
        default=CONSULTA
    )
    
    def __str__(self):
        return f"{self.tipoEvento} - Fecha: {self.fechaEvento}"


