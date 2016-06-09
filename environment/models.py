from django.db import models
from headquarters.models import Headquarters
# Create your models here.
class EnvironmentType(models.Model):

    name        = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    status      = models.IntegerField()

class Environment(models.Model):

    environment_type = models.ForeignKey(EnvironmentType,on_delete=models.CASCADE,default=None)
    headquarters 	= models.ForeignKey(Headquarters,on_delete=models.CASCADE,default=None)

    name = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    capacity = models.IntegerField()
    status = models.IntegerField()