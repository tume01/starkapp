from django.db import models

# Create your models here.

class ActivitiesType(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Activity(models.Model):
    end_date = models.DateTimeField()
    attendance = models.IntegerField()
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)