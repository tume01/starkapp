from bungalow_raffle.models import BungalowRaffle
from repositories.BaseRepository import BaseRepository 

class BungalowRaffleRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, BungalowRaffle)
