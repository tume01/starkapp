
from fine.models import Fine
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class FineRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Fine)
