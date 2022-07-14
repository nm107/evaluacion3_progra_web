from django.db import models
import datetime
from django.utils import timezone


class Persona(models.Model):
    rut = models.CharField(max_length=10, null=False, blank=False)
    nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    edad = models.IntegerField()
    
    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.nombre,self.rut)


class Vacuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_vacuna = (
        ("Pfizer", "Pfizer"),
        ("Sinovac", "Sinovac"),
        ("AstraZeneca", "AstraZeneca"),
        ("CanSino", "CanSino"),
        ("Janssen", "Janssen"),
        ("SPUTNIK-V", "SPUTNIK-V"),
        ("Moderna", "Moderna")
    )
    nombre = models.CharField(max_length=30,
                             choices=nombre_vacuna,
                             default="Moderna")
    
    def __str__(self):
        return '{}-{}'.format(self.id, self.nombre)

class Vacunacion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    vacuna_CHOICES = (
        ("1", "Primera Docis"),
        ("2", "Segunda Docis"),
        ("3", "Tercera Docis"),
        ("4", "Cuarta Docis"),
    )
    dosis = models.CharField(max_length=30,
                             choices=vacuna_CHOICES,
                             default="primera_docis")
    fecha = models.DateTimeField('date published',default=timezone.now())

    def was_published_recently(self):
        return self.fecha >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.persona,self.vacuna)

class PaseDeMovilidad(models.Model):
    fecha_inicio = models.DateTimeField('date published',default=timezone.now())
    fecha_termino = models.DateTimeField('date published',default=timezone.now())
    vacunatorio = models.CharField(max_length=100)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField('date published',default=timezone.now())

    