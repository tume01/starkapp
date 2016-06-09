from django.db import models
from memberships import models as y

# Create your models here.
class Suspension(models.Model):
    membership = models.ForeignKey(y.Membership, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    initialDate = models.DateField()
    finalDate = models.DateField()
    status = models.IntegerField()