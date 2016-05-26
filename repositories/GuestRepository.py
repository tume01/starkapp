from guests.models import Guest
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class GuestRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Guest)

    def all(self):
        return self.model.objects.filter(status=1)