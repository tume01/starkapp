from django.db import models
from members import models as x
from django.contrib.auth.models import User
from identity_document_type import models as z
from ubigeo import models as y
# Create your models here.


class Relationship(models.Model):
    description = models.TextField(max_length=200)

class Affiliate(models.Model):
    member = models.ForeignKey(x.Member, on_delete=models.CASCADE)
    identity_document_type = models.ForeignKey(z.Identity_Document_Type, on_delete=models.CASCADE)
    ubigeo = models.ForeignKey(y.Ubigeo, related_name='affiliate_address_ubigeo', on_delete=models.CASCADE)
    name=models.TextField(max_length=200)
    paternalLastName=models.TextField(max_length=200)
    maternalLastName=models.TextField(max_length=200)
    document_number=models.IntegerField()
    phone=models.IntegerField()
    address=models.TextField(max_length=200)
    email=models.TextField(max_length=200)
    state=models.IntegerField()
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)

    gender = models.IntegerField()  # 0 masculino 1 femenino
    nationality = models.TextField(max_length=20)
    birthDate = models.DateField()
    birthPlace = models.TextField(max_length=200)
    photo = models.ImageField(upload_to='affiliate')
    specialization = models.TextField(max_length=200, blank=True, null=True)
    workPlace = models.TextField(max_length=200, blank=True, null=True)
    workPlaceJob = models.TextField(max_length=200, blank=True, null=True)
    workPlacePhone = models.IntegerField(blank=True, null=True)
    maritalStatus = models.TextField(max_length=20)
    cellphoneNumber = models.IntegerField(blank=True, null=True)
