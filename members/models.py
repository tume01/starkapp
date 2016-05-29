from django.db import models
from memberships import models as x
from users import models as y

# Create your models here.
class Member(models.Model):
    membership = models.ForeignKey(x.Membership, on_delete=models.CASCADE)
    user = models.ForeignKey(y.User, on_delete=models.CASCADE)
    name=models.TextField(max_length=200)
    surname=models.TextField(max_length=200)
    dni=models.IntegerField()
    phone=models.IntegerField()
    address=models.TextField(max_length=200)
    email=models.TextField(max_length=200)
    state=models.IntegerField()
