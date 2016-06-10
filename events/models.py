from django.db import models
from events_type.models import EventsType
from environment.models import Environment
from headquarters.models import Headquarters
from users.models import User

class Event(models.Model):
    event_type  =   models.ForeignKey(EventsType, on_delete=models.CASCADE,default=None)
    environment =   models.ManyToManyField(Environment)
    user        =   models.ManyToManyField(User)
    headquarter =   models.ForeignKey(Headquarters, on_delete=models.CASCADE,default=None)

    name        =   models.CharField(max_length=100)
    description =   models.CharField(max_length=200)
    ruc         =   models.CharField(max_length=8)
    seat        =   models.CharField(max_length=20)
    start_date  =   models.DateTimeField()
    end_date    =   models.DateTimeField()
    assistance  =   models.IntegerField()
    price_member=   models.FloatField()
    price_invited=  models.FloatField()
    status      =   models.IntegerField()