
from politics.models import Politic
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class PoliticsRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Politic)


   