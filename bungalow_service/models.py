from django.db import models
#from bungalow_type.models import BungalowType

# Create your models here.

class Bungalow_service(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	pay_per_hour = models.BooleanField(default=False)
	pay_per_day = models.BooleanField(default=False)
	pay_unique = models.BooleanField(default=False)
	price = models.FloatField()
	deleted_at = models.DateTimeField(null=True)
	#bungalow_type = models.ManyToManyField(BungalowType)


