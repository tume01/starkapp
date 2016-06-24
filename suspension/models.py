from django.db import models
from memberships import models as y

# Create your models here.
class SuspensionType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.IntegerField()

class Suspension(models.Model):
    suspension_type = models.ForeignKey(SuspensionType, on_delete=models.CASCADE)
    membership = models.ForeignKey(y.Membership, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    initialDate = models.DateField()
    finalDate = models.DateField()
    status = models.IntegerField()

