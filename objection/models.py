from django.db import models as x
from membership_application import models as y
from members import models as z

# Create your models here.
class Objection(x.Model):
    membership_application = x.ForeignKey(y.Membership_Application, on_delete=x.CASCADE)
    member = x.ForeignKey(z.Member, on_delete=x.CASCADE)
    date = x.DateField()
    comments=x.TextField(max_length=200)
    status=x.IntegerField()
