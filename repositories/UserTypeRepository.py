from users.models import UserType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class UserTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, UserType)


   
