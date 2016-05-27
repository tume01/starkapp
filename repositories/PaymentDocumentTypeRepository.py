from payment_documents.models import Payment_Document_Type
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class PaymentDocumentTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Payment_Document_Type)

    def all(self):
        return self.model.objects.filter(status=1)