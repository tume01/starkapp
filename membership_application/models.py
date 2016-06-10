from django.db import models as m
from memberships import models as x
from identity_document_type import models as y

# Create your models here.
class Membership_Application(m.Model):
    membership_type = m.ForeignKey(x.MembershipType, on_delete=m.CASCADE)
    identity_document_type = m.ForeignKey(y.Identity_Document_Type, on_delete=m.CASCADE)
    firstName = m.CharField(max_length=20)
    paternalLastName = m.CharField(max_length=20)
    maternalLastName = m.CharField(max_length=20)
    document_number = m.IntegerField()
    comments = m.CharField(max_length=200)
    initialDate = m.DateField()
    finalDate = m.DateField()
    status = m.IntegerField()
    #0 = Eliminado, 1 = En espera, 2 = Aceptado, 3 = Rechazado
