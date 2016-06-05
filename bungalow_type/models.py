from django.db import models

class BungalowType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.FloatField()
    capacity = models.IntegerField()
    
    deleted_at = models.DateTimeField(null=True)

