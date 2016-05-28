from bungalows.models import Bungalow
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class BungalowsRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Bungalow) 