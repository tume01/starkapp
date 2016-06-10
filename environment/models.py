from django.db import models
from headquarters.models import Headquarters

# Create your models here.
class Environment(models.Model):
    #sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    capacity = models.IntegerField()
    status = models.IntegerField()

    headquarter = models.ForeignKey(Headquarters, on_delete=models.CASCADE)


class EnvironmentReservation(models.Model):
    environment  = models.ForeignKey(Environment, on_delete=models.CASCADE)
    end_date     = models.DateTimeField()
    start_date   = models.DateTimeField()
    price        = models.DecimalField(max_digits=6, decimal_places=2)
    status       = models.IntegerField()