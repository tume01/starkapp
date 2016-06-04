from ubigeo.models import Ubigeo
from .BaseRepository import BaseRepository

class UbigeoRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Ubigeo)