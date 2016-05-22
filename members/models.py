from django.db import models

# Create your models here.
class Member(models.Model):

    name=models.TextField(max_length=200)
    surname=models.TextField(max_length=200)
    dni=models.TextField(max_length=200)
    phone=models.IntegerField()
    address=models.TextField(max_length=200)
    email=models.TextField(max_length=200)
    state=models.IntegerField()
