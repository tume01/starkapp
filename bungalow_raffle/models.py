from django.db import models

# Create your models here.

class BungalowRaffle(models.Model):
    bungalow_id = models.IntegerField(null=True)
    bungalow_number = models.IntegerField()

    bungalow_type_id = models.IntegerField(null=True)
    bungalow_type_name = models.CharField(max_length=250)

    bungalow_headquarter_id = models.IntegerField(null=True)
    bungalow_headquarter_name = models.CharField(max_length=250)

    member_id = models.IntegerField(null=True)
    member_membership_name = models.TextField(max_length=200)
    member_name = models.TextField(max_length=200)
    member_paternalLastName = models.TextField(max_length=200)
    member_maternalLastName = models.TextField(max_length=200)

    arrival_date = models.DateField(null=True)

    deleted_at = models.DateTimeField(null=True)