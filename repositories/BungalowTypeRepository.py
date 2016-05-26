from bungalows.models import BungalowType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class BungalowTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, BungalowType)
