from django.db import models
from bungalow_service.models import Bungalow_service

class BungalowType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.FloatField()
    capacity = models.IntegerField()
    
    deleted_at = models.DateTimeField(null=True)

    bungalow_services = models.ManyToManyField(Bungalow_service)

