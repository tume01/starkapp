from bungalow.models import Bungalow
from repositories.BaseRepository import BaseRepository 

class BungalowRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, Bungalow) 
