from django.db import models
from members.models import Member
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

class CartProduct(models.Model):

    PRODUCT_CHOICES = (
        (1, 'Multa'),
        (2, 'Membresia'),   
        (3, 'Evento'),
        (4, 'Reserva Bungalow'),
        (5, 'Evento Invitado')
    )

    description = models.TextField()
    quantity = models.IntegerField()
    product_type = models.IntegerField(choices=PRODUCT_CHOICES)
    product_id = models.IntegerField()
    status = models.IntegerField(default=0)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    discount = models.FloatField()
    total = models.FloatField()
    unit_price = models.FloatField()