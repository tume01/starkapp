from django.db import models
from memberships import models.Membership

# Create your models here.
class Member(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    name=models.TextField(max_length=200)
    surname=models.TextField(max_length=200)
    dni=models.IntegerField()
    phone=models.IntegerField()
    address=models.TextField(max_length=200)
    email=models.TextField(max_length=200)
    state=models.IntegerField()
