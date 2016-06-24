from payment_documents.models import Invoice
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class InvoiceRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Invoice)
