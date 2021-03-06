from django.db import models
from django.forms import ModelChoiceField
from headquarters.models import Headquarters

class EnvironmentType(models.Model):


    name        = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    status      = models.IntegerField()

class Environment(models.Model):

    status_choices = ((0,'Inactivo'),(1,'Activo'),)
    court_choices = ((0,'Fútbol'),(1,'Básquet'),(2,'Voley'))
    environment_type = models.ForeignKey(EnvironmentType,on_delete=models.CASCADE,default=None, null=True)
    name = models.TextField(max_length=100)
    description = models.CharField(null=False, blank=False,max_length=200)
    capacity = models.BigIntegerField(null=False, blank=False)
    status = models.IntegerField(choices=status_choices,default=1) #Binario por estado 0->Inactivo 1->Activo  
    court_type  = models.IntegerField(choices=court_choices,default=1)
    headquarter = models.ForeignKey(Headquarters, on_delete=models.CASCADE)


class EnvironmentReservation(models.Model):
    environment  = models.ForeignKey(Environment, on_delete=models.CASCADE)
    end_date     = models.DateTimeField()
    start_date   = models.DateTimeField()
    price        = models.DecimalField(max_digits=6, decimal_places=2)
    status       = models.IntegerField()

    def getReservationDays(self):
        d1 = self.start_date
        d2 = self.end_date

        dd = [d1 + datetime.timedelta(days=d) for d in range((d2 - d1).days + 1)]
        reserved = [int(day.strftime('%Y%m%d')) for day in dd]

        return reserved
