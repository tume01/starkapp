
from django.db import models

from bungalow_service.models import Bungalow_service

class Bungalow(models.Model):
    STATUS_CHOICES = (
        (1, 'Disponible'),
        (2, 'Mantenimiento'),
        (3, 'Proximamente'),
        (4, 'Detenido'),
    )

    bungalow_type = models.ForeignKey('bungalow_type.BungalowType', on_delete=models.CASCADE)
    headquarter = models.ForeignKey('headquarters.Headquarters', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES)
    location = models.CharField(max_length=200)
    number = models.IntegerField()

    deleted_at = models.DateTimeField(null=True)

    bungalow_services = models.ManyToManyField(Bungalow_service)

    def getStatusName(self):
        index = self.status - 1
        statusData = self.STATUS_CHOICES[index]
        return statusData[1]