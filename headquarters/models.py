from django.db import models
from ubigeo.models import Ubigeo

# Create your models here.

class Headquarters(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length = 250)
    location = models.CharField(max_length=250)
    status = models.IntegerField()
    ubigeos = models.ForeignKey(Ubigeo, on_delete=models.CASCADE)