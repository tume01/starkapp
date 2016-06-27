from django.db import models as m
from memberships import models as x
from identity_document_type import models as y
from ubigeo import models as z

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

    photo = m.ImageField(upload_to='membership_application')
    address = m.TextField(max_length=200)
    gender = m.IntegerField() #0 masculino 1 femenino
    workPlace = m.TextField(max_length=200)
    workPlaceJob = m.TextField(max_length=200)
    workPlacePhone = m.IntegerField()
    nationality = m.TextField(max_length=20)
    maritalStatus = m.TextField(max_length=20)
    cellphoneNumber = m.IntegerField()
    specialization = m.TextField(max_length=200)
    birthDate = m.DateField()
    birthPlace = m.TextField(max_length=200)
    email=m.TextField(max_length=200)
    phone=m.IntegerField()
    ubigeo = m.ForeignKey(z.Ubigeo, related_name='app_address_ubigeo', on_delete=m.CASCADE)
    birthUbigeo = m.ForeignKey(z.Ubigeo, related_name='app_birth_ubigeo', on_delete=m.CASCADE)

    #conyuge
    sidentity_document_type = m.ForeignKey(y.Identity_Document_Type, related_name='identity_doc_spouse', blank=True, null=True, on_delete=m.CASCADE)
    sfirstName = m.CharField(max_length=20, blank=True, null=True)
    spaternalLastName = m.CharField(max_length=20, blank=True, null=True)
    smaternalLastName = m.CharField(max_length=20, blank=True, null=True)
    sdocument_number = m.IntegerField(blank=True, null=True)
    sgender = m.IntegerField(blank=True, null=True) #0 masculino 1 femenino
    sspecialization = m.TextField(max_length=200, blank=True, null=True)
    snationality = m.TextField(max_length=20, blank=True, null=True)
    sbirthDate = m.DateField(blank=True, null=True)
    sbirthPlace = m.TextField(max_length=200, blank=True, null=True)
    sphoto = m.ImageField(upload_to='membership_application', blank=True, null=True)
    sworkPlace = m.TextField(max_length=200, blank=True, null=True)
    sworkPlaceJob = m.TextField(max_length=200, blank=True, null=True)
    sworkPlacePhone = m.IntegerField(blank=True, null=True)
    scellPhoneNumber = m.IntegerField(blank=True, null=True)
    semail=m.TextField(max_length=200, blank=True, null=True)
    sbirthUbigeo = m.ForeignKey(z.Ubigeo, blank=True, null=True,related_name='spouse_birth_ubigeo', on_delete=m.CASCADE)

    status = m.IntegerField()
    #0 = Eliminado, 1 = En espera, 2 = Aceptado, 3 = Rechazado
