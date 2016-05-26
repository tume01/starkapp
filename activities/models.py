from django.db import models
from activity_types.models import ActivityType
# Create your models here.

class Activity(models.Model):
    end_date = models.DateTimeField()
    attendance = models.IntegerField()
    start_date = models.DateTimeField()
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    activity_type= models.ForeignKey(ActivityType, on_delete=models.CASCADE)