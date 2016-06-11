from django.db import models
from payment_documents import models as x
from members import models as y
from affiliate import models as affiliates
from guests import models as guests

class Entry(models.Model):
    payment_document = models.ForeignKey(x.Payment_Document, blank=True, null=True, on_delete=models.CASCADE)
    member = models.ForeignKey(y.Member, blank=True, null=True,on_delete=models.CASCADE)
    affiliate = models.ForeignKey(affiliates.Affiliate, blank=True, null=True,on_delete=models.CASCADE)
    guest= models.ForeignKey(guests.Guest, blank=True, null=True,on_delete=models.CASCADE)
    initialDate = models.DateField()
    finalDate = models.DateField()