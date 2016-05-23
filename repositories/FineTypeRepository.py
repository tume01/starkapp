from fine.models import FineType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class FineTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, FineType)

    def all(self):
        return self.model.objects.filter(status=1)