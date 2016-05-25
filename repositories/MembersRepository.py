from members.models import Member
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class MembersRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Member)

    def all(self):
        return self.model.objects.filter(state=1)


   
