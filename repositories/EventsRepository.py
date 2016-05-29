from events.models 			import Event
from contracts.repositories import AbstractBaseRepository
from .BaseRepository 		import BaseRepository 

class EventsRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Event)


   