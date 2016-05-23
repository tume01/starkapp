from activities.models import Activity
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class ActivityRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Activity)


   