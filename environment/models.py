from django.db import models
from django.forms import ModelChoiceField

# Create your models here.
class Environment(models.Model):
    #headquarter = models.ForeignKey("Headquarters", on_delete=models.CASCADE)
    status_choices = ((0,'Inactivo'),(1,'Activo'),)

    name = models.CharField(null=False, blank=False,max_length=100)
    description = models.CharField(null=False, blank=False,max_length=200)
    capacity = models.BigIntegerField(null=False, blank=False)
    status = models.IntegerField(choices=status_choices,default=1) #Binario por estado 0->Inactivo 1->Activo    
