from django.db import models
from providers.models import Provider

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    provider = models.ManyToManyField(Provider)
    #purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    price = models.FloatField()
    actual_stock = models.IntegerField()
    minimum_stock = models.IntegerField()
    status = models.IntegerField()
    description = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=20, default='')
