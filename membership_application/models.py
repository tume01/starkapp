from django.db import models
from memberships import models.MembershipType

# Create your models here.
class Membership_Application(models.Model):
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    dni = models.IntegerField()
    comments = models.CharField(max_length=200)
    initialDate = models.DateField()
    finalDate = models.DateField()
    status = models.CharField(max_length=20)
