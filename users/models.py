from django.db import models

# Create your models here.
class UserType(models.Model):
    description = models.TextField(max_length=200)

class User(models.Model):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    name = models.TextField(max_length=200)
    password = models.TextField(max_length=200)
