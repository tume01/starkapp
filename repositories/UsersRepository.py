from users.models import User
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class UsersRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, User)


   
