from django.db import models

# Create your models here.

class Politic(models.Model):

    name = models.CharField(max_length=100)
    value = models.FloatField()
    deleted_at = models.DateTimeField(null=True)
