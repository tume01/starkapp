from django.db import models

# Create your models here.
class Guest(models.Model):
    name=models.TextField(max_length=200)
    paternalLastName=models.TextField(max_length=200)
    document_number=models.IntegerField()
    status=models.IntegerField()
