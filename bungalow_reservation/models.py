from django.db import models

class BungalowReservation(models.Model):

    bungalow = models.ForeignKey('bungalow.Bungalow', on_delete=models.CASCADE, null=True)
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE, null=True)
    payment_document = models.ForeignKey('payment_documents.Payment_Document', on_delete=models.CASCADE, null=True)
    
    arrival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)

    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)
    price = models.FloatField(null=True)

    deleted_at = models.DateTimeField(null=True)