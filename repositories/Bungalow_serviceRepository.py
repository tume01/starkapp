from bungalow_service.models import Bungalow_service
from repositories.BaseRepository import BaseRepository

class Bungalow_serviceRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, Bungalow_service)

