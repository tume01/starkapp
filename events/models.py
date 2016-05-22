from django.db import models

# Create your models here.

class EventType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

class Event(models.Model):
    event_type_id   =   models.ForeignKey(EventType, on_delete=models.CASCADE)
    #environment    =   models.ForeignKey(Environment, on_delete=models.CASCADE)
    #user           =   models.ForeignKey(User, on_delete=models.CASCADE)

    name        =   models.CharField(max_length=100)
    description =   models.CharField(max_length=200)
    start_date  =   models.DateField()
    end_date    =   models.DateField()
    assistance  =   models.IntegerField()
    price       =   models.FloatField()
    status      =   models.IntegerField()