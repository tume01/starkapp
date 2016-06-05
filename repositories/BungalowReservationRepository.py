from bungalow_reservation.models import BungalowReservation
from repositories.BaseRepository import BaseRepository 

class BungalowReservationRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, BungalowReservation) 
