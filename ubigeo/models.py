from django.db import models

class Ubigeo(models.Model):
    department = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
# Create your models here.
