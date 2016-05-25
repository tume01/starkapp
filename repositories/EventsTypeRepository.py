from events_type.models 			import EventsType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository 		import BaseRepository 

class EventsTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, EventsType)