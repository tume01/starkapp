from django.db import models
from headquarters.models import Headquarters
from django.contrib.auth.models import User

# Create your models here.
class FieldReservation(models.Model):

    headquarter          = models.ForeignKey(Headquarters, on_delete=models.CASCADE)

    court_name              = models.TextField(max_length=100)
    court_headquarter_name  = models.TextField(max_length=100)
    court_type              = models.IntegerField()

    user             = models.ForeignKey(User,on_delete=models.CASCADE)
    member_membership_name  = models.TextField(max_length=200)
    member_name= models.TextField(max_length=200)
    member_paternalLastName = models.TextField(max_length=200)
    member_maternalLastName = models.TextField(max_length=200)

    reservation_duration    = models.IntegerField()
    reservation_date        = models.DateTimeField(null=True)
    
    status                  = models.IntegerField()

    deleted_at              = models.DateTimeField(null=True)