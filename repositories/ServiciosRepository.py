
from servicios.models import Servicio
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class ServiciosRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Servicio)


   