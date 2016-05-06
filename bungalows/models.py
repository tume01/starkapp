from django.db import models

# Create your models here.
class TipoBungalow(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    precio = models.FloatField()
    aforo = models.IntegerField()

class Bungalow(models.Model):
    tipoBungalow = models.ForeignKey(TipoBungalow, on_delete=models.CASCADE)
    #ambiente = models.ForeignKey("Ambiente", on_delete=models.CASCADE)

    estado = models.IntegerField()
    ubicacion = models.CharField(max_length=200)
    numero = models.IntegerField()