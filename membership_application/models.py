from django.db import models

# Create your models here.
class Membership_Application(models.Model):
    comments = models.CharField(max_length=200)
    status=models.CharField(max_length=20)
