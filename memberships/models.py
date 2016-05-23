from django.db import models

# Create your models here.

class MembershipType(models.Model):
    name = models.TextField(max_length=200)
    guests = models.IntegerField()
    price = models.FloatField()
    billing = models.TextField(max_length=200)
    status = models.IntegerField()
    
