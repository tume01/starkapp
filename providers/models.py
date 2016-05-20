from django.db import models

# Create your models here.

class Provider(models.Model):    
    #ambiente = models.ForeignKey("Ambiente", on_delete=models.CASCADE)
    idProvider = models.IntegerField()
    ruc = models.BigIntegerField()
    businessName = models.CharField(max_length=200)
    status = models.IntegerField() #Binario por estado 0->Inactivo 1->Activo    
    province = models.CharField(max_length=100)
    distric = models.CharField(max_length=100)
    registrationDate = models.DateField(auto_now=False, auto_now_add=True)
    address = models.CharField(max_length=200)    
    phone= models.BigIntegerField()
    effectiveTime = models.IntegerField() #Tiempo de vigencia en días
    email= models.EmailField()    
    contactName = models.CharField(max_length=100)
    contactPhone = models.BigIntegerField()
    