from django.db import models
from environment import models as x

class BungalowType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.FloatField()
    capacity = models.IntegerField()

class Bungalow(models.Model):
    bungalow_type = models.ForeignKey(BungalowType, on_delete=models.CASCADE)
    #environment = models.ForeignKey(x.Environment, on_delete=models.CASCADE)
    status = models.IntegerField()
    location = models.CharField(max_length=200)
    number = models.IntegerField()