from django.db import models
from events_type.models import EventsType

class Event(models.Model):
    event_type  =   models.ForeignKey(EventsType, on_delete=models.CASCADE,default=None)
    #environment =   models.ForeignKey(Environment, on_delete=models.CASCADE)
    #user        =   models.ForeignKey(User, on_delete=models.CASCADE)

    name        =   models.CharField(max_length=100)
    description =   models.CharField(max_length=200)
    ruc         =   models.CharField(max_length=8)
    seat        =   models.CharField(max_length=20)
    start_date  =   models.DateField()
    end_date    =   models.DateField()
    assistance  =   models.IntegerField()
    price       =   models.FloatField()
    status      =   models.IntegerField()