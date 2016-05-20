from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.TextField(max_length=200)
    discount_percentage = models.FloatField()
