from activity_types.models import ActivityType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class ActivityTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, ActivityType)