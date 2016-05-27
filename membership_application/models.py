from django.db import models as m
from memberships import models as x

# Create your models here.
class Membership_Application(m.Model):
    membership_type = m.ForeignKey(x.MembershipType, on_delete=m.CASCADE)
    firstName = m.CharField(max_length=20)
    lastName = m.CharField(max_length=20)
    dni = m.IntegerField()
    comments = m.CharField(max_length=200)
    initialDate = m.DateField()
    finalDate = m.DateField()
    status = m.IntegerField()
