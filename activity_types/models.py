from django.db import models

# Create your models here.
class ActivityType(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)