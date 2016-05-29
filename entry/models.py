from django.db import models
from payment_documents import models as x
from members import models as y

class Entry(models.Model):
    payment_document = models.ForeignKey(x.Payment_Document, on_delete=models.CASCADE)
    member = models.ForeignKey(y.Member, on_delete=models.CASCADE)
    initialDate = models.DateField()
    finalDate = models.DateField()
    numberOfGuests = models.IntegerField()
