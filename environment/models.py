from django.db import models

# Create your models here.
class Environment(models.Model):
    #sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    capacity = models.IntegerField()
    status = models.IntegerField()