from django.db import models

# Create your models here.

class MembershipType(models.Model):
    name = models.TextField(max_length=200)
    guests = models.IntegerField()
    price = models.FloatField()
    billing = models.TextField(max_length=200)
    status = models.IntegerField()

class Membership(models.Model):
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    initialDate = models.DateField()
    finalDate = models.DateField()
    status = models.IntegerField()

