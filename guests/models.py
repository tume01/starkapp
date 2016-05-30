from django.db import models
from entry import models as x

# Create your models here.
class Guest(models.Model):
    entry = models.ForeignKey(x.Entry, on_delete=models.CASCADE)
    name=models.TextField(max_length=200)
    surname=models.TextField(max_length=200)
    dni=models.IntegerField()
    status=models.IntegerField()
