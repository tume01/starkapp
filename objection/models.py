from django.db import models
from membership_application import models.Membership_Application

# Create your models here.
class Objection(models.Model):
    membership_application = models.ForeignKey(Membership_Application, on_delete=models.CASCADE)
    comments=models.TextField(max_length=200)
