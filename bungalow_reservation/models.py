from django.db import models
import datetime
class BungalowReservation(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendiente'),
        (1, 'Reservada'),
        (2, 'En uso'),
        (4, 'Finalizada'),
    )

    # bungalow = models.ForeignKey('bungalow.Bungalow', on_delete=models.CASCADE, null=True)
    # Changed because persistence issues
    bungalow_number = models.IntegerField()
    bungalow_price = models.FloatField()
    bungalow_capacity = models.IntegerField()
    bungalow_type_id = models.IntegerField()
    bungalow_headquarter_id = models.IntegerField()
    bungalow_headquarter_name = models.CharField(max_length=250)

    # member = models.ForeignKey('members.Member', on_delete=models.CASCADE, null=True)
    # Changed because persistence issues
    member_membership_name = models.TextField(max_length=200)
    member_name = models.TextField(max_length=200)
    member_paternalLastName = models.TextField(max_length=200)
    member_maternalLastName = models.TextField(max_length=200)
    # member_document_number = models.IntegerField()
    # member_phone = models.IntegerField()
    # TODO: Wait to seeder

    payment_document = models.ForeignKey('payment_documents.Payment_Document', on_delete=models.CASCADE, null=True)
    # TODO: Change because persistence issues

    arrival_date = models.DateField(null=True)
    departure_date = models.DateField(null=True)

    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)

    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    deleted_at = models.DateTimeField(null=True)

    def getStatusName(self):
        index = self.status
        statusData = self.STATUS_CHOICES[index]
        return statusData[1]

    def getDays(self):
        days = []

        for date in range((self.departure_date - self.arrival_date).days + 1):
            days.append(self.arrival_date + datetime.timedelta(days=date))

        return days


