
from membership_application.models import Membership_Application
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class Membership_ApplicationRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Membership_Application)
