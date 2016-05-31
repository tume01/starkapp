from django.db import models

# Create your models here.
class ServicioType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)


class Servicio(models.Model):
    servicio_type = models.ForeignKey(ServicioType, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    price = models.FloatField()
    deleted = models.BooleanField(default=False)
