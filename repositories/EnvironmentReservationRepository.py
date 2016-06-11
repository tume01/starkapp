from environment.models import EnvironmentReservation
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository


class EnvironmentReservationRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, EnvironmentReservation)




