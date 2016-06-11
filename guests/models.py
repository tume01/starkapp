from django.db import models

# Create your models here.
class Guest(models.Model):
    name=models.TextField(max_length=200)
    surname=models.TextField(max_length=200)
    dni=models.IntegerField()
    status=models.IntegerField()
