from django.db import models

# Create your models here.
class Membership_Application(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    dni = models.IntegerField()
    comments = models.CharField(max_length=200)
    initialDate = models.DateField()
    finalDate = models.DateField()
    status = models.CharField(max_length=20)
