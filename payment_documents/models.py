from django.db import models

# Create your models here.

class Payment_Document_Type(models.Model):
    name = models.TextField(max_length=200)
    descripcion = models.TextField(max_length=200)

class Payment_Document(models.Model):
    payment_document_type = models.ForeignKey(Payment_Document_Type, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=200)
    amount = models.FloatField()
    igv = models.FloatField()
    realAmount = models.FloatField()

class Ticket(models.Model):
    products = models.TextField()
    subtotal = models.FloatField()
    discounts = models.FloatField()
    igv_amount = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField()

class Invoice(models.Model):
    products = models.TextField()
    subtotal = models.FloatField()
    discounts = models.FloatField()
    igv_amount = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField()
    name = models.TextField()
    address = models.TextField()
    ruc = models.IntegerField()