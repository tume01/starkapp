from django.db import models

# Create your models here.

class Provider(models.Model):    
    #ambiente = models.ForeignKey("Ambiente", on_delete=models.CASCADE)

    status_choices = ((0,'Inactivo'),(1,'Activo'),)

    ruc = models.BigIntegerField()
    businessName = models.CharField(max_length=200)
    status = models.IntegerField(choices=status_choices,default=1) #Binario por estado 0->Inactivo 1->Activo    
    province = models.CharField(max_length=120)
    distric = models.CharField(max_length=120)
    registrationDate = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=200)    
    phone= models.BigIntegerField()
    effectiveTime = models.IntegerField() #Tiempo de vigencia en días
    email= models.EmailField()    
    contactName = models.CharField(max_length=120)
    contactPhone = models.BigIntegerField()