from reserve_field.models import FieldReservation
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class FieldReservationRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, FieldReservation)