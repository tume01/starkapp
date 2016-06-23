from django.db import models
from events_type.models import EventsType
from environment.models import Environment
from headquarters.models import Headquarters
from members.models import Member

class Event(models.Model):
    event_type  =   models.ForeignKey(EventsType, on_delete=models.CASCADE,default=None)
    environment =   models.ManyToManyField(Environment)
    creator     =   models.ForeignKey(Member, on_delete=models.CASCADE,default=None, related_name='member_creator')
    headquarter =   models.ForeignKey(Headquarters, on_delete=models.CASCADE,default=None)
    name        =   models.CharField(max_length=100)
    description =   models.CharField(max_length=200)
    ruc         =   models.CharField(max_length=8)
    seat        =   models.CharField(max_length=20)
    start_date  =   models.DateTimeField()
    end_date    =   models.DateTimeField()
    assistance  =   models.IntegerField()
    price_member =   models.FloatField()
    price_invited =  models.FloatField()
    status      =   models.IntegerField()
    members = models.ManyToManyField(
        Member,
        through="EventRegistration",
        through_fields=('event', 'member'),
    )

class EventRegistration(models.Model):
    registered_at = models.DateTimeField(null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True)