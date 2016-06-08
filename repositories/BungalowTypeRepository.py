from bungalow_type.models import BungalowType
from repositories.BaseRepository import BaseRepository

class BungalowTypeRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, BungalowType)

