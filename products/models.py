from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    #provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    #purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    price = models.FloatField()
    anual_stock = models.IntegerField()
    minimum_stock = models.IntegerField()
    status = models.IntegerField()
