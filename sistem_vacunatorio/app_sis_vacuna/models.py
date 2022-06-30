from django.db import models
import datetime
from django.utils import timezone


class Persona(models.Model):
    rut = models.CharField(max_length=10, null=False, blank=False)
    nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    edad = models.IntegerField()
    nombre_vacuna = models.CharField(max_length=50)
    fecha = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.fecha >= timezone.now() - datetime.timedelta(days=1)


class Vacuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_vacuna = (
        ("pfizer", "Pfizer"),
        ("Sinovac", "Sinovac"),
        ("AstraZeneca", "AstraZeneca"),
        ("CanSino", "CanSino"),
        ("Janssen", "Janssen"),
        ("SPUTNIK-V", "SPUTNIK-V"),
        ("Moderna", "Moderna"),
        ("Janssen", "Janssen"),
    )
    nombre = models.CharField(max_length=30,
                             choices=nombre_vacuna,
                             default="Moderna")

class Vacunacion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    vacuna_CHOICES = (
        ("primera_docis", "Primera Docis"),
        ("segunda_docis", "Segunda Docis"),
        ("tercera_docis", "Tercera Docis"),
        ("cuarta_docis", "Cuarta Docis"),
    )
    dosis = models.CharField(max_length=30,
                             choices=vacuna_CHOICES,
                             default="primera_docis")
