from payment_documents.models import Payment_Document
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class PaymentDocumentRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Payment_Document)

    def all(self):
        return self.model.objects.filter(status=1)