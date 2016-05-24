from django.db import models as x
from membership_application import models as y

# Create your models here.
class Objection(x.Model):
    membership_application = x.ForeignKey(y.Membership_Application, on_delete=x.CASCADE)
    comments=x.TextField(max_length=200)
