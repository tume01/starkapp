from django.db import models
from environment.models import Environment
from activity_types.models import ActivityType
from members.models import Member
# Create your models here.

class Activity(models.Model):
    deleted_at = models.DateTimeField(null=True)
    end_date = models.DateTimeField()
    attendance = models.IntegerField()
    start_date = models.DateTimeField()
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    activity_type= models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    enviroment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    members = models.ManyToManyField(
        Member,
        through='ActivityRegistration',
        through_fields=('activity', 'member'),
    )

class ActivityRegistration(models.Model):
    register_day = models.DateTimeField(null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
 
