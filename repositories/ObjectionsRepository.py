from objections.models import Objection
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class ObjectionsRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, User)


   
