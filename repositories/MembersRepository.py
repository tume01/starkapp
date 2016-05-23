from members.models import Member
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class MembersRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Member)


   
