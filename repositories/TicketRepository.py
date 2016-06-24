from payment_documents.models import Ticket
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class TicketRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Ticket)
