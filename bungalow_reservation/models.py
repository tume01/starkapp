from django.db import models
import datetime

from bungalow.models import Bungalow
from members.models import Member
from bungalow_service.models import Bungalow_service

class BungalowReservation(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendiente'),
        (1, 'Reservada'),
        (2, 'En uso'),
        (4, 'Finalizada'),
    )

    #bungalow = models.ForeignKey('bungalow.Bungalow', on_delete=models.CASCADE, null=True)
    # Changed because persistence issues
    bungalow_number = models.IntegerField()
    bungalow_price = models.FloatField()
    bungalow_capacity = models.IntegerField()
    bungalow_type_id = models.IntegerField(null=True)
    bungalow_headquarter_id = models.IntegerField(null=True)
    bungalow_headquarter_name = models.CharField(max_length=250)

    #member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    # Changed because persistence issues
    member_membership_name = models.TextField(max_length=200)
    member_name = models.TextField(max_length=200)
    member_paternalLastName = models.TextField(max_length=200)
    member_maternalLastName = models.TextField(max_length=200)


    bungalow_id = models.IntegerField(null=True)
    member_id = models.IntegerField(null=True)

    payment_document = models.ForeignKey('payment_documents.Payment_Document', on_delete=models.CASCADE, null=True)
    # TODO: Change because persistence issues

    arrival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)

    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    deleted_at = models.DateTimeField(null=True)

    aditional_services = models.ManyToManyField(Bungalow_service)

    def getStatusName(self):
        index = self.status
        statusData = self.STATUS_CHOICES[index]
        return statusData[1]

    def getReservationDays(self):
        d1 = self.arrival_date
        d2 = self.departure_date
        dd = [d1 + datetime.timedelta(days=d) for d in range((d2 - d1).days + 1)]

        reserved = [int(day.strftime('%Y%m%d')) for day in dd]

        print(reserved)
        return reserved
