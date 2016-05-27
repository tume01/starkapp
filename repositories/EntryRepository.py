from entry.models import Entry
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class EntryRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Entry)

    def all(self):
        return self.model.objects.filter(status=1)