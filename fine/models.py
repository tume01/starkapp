from django.db import models

# Create your models here.
class FineType(models.Model):
    #name = models.CharField(max_length=100)
    reason = models.TextField(max_length=200)
    price = models.FloatField()
    #capacity = models.IntegerField()

class Fine(models.Model):
    fine_type_id = models.ForeignKey(FineType, on_delete=models.CASCADE)
    #ambiente = models.ForeignKey("Ambiente", on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    observations = models.CharField(max_length=200)    
