from django.db import models

# Create your models here.

class EventsType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    status = models.IntegerField() #inhabilitado habilitado