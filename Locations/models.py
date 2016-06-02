from django.db import models


# Create your models here.

class Region(models.Model):      
    name = models.CharField(max_length=100)

class Province(models.Model):
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

class District(models.Model):
	province = models.ForeignKey(Province, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)