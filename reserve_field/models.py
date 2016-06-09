from django.db import models

# Create your models here.
class FieldReservation(models.Model):

    court_name              = models.TextField(max_length=100)
    court_headquarter_name  = models.TextField(max_length=100)

    member_membership_name  = models.TextField(max_length=200)
    member_name= models.TextField(max_length=200)
    member_paternalLastName = models.TextField(max_length=200)
    member_maternalLastName = models.TextField(max_length=200)

    reservation_hour        = models.TimeField(null=True)
    reservation_duration    = models.IntegerField()
    reservation_date        = models.DateField(null=True)
    
    status                  = models.IntegerField()

    deleted_at              = models.DateTimeField(null=True)