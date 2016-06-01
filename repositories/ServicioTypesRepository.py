
from servicios.models import ServicioType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class ServicioTypesRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, ServicioType)


   