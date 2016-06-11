from events.models 			import Event
from events.models          import EventRegistration
from contracts.repositories import AbstractBaseRepository
from .BaseRepository        import BaseRepository 
from datetime import datetime

class EventsRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Event)

    def addMember(self, event, member):
        registration = EventRegistration(event=event, member=member, registered_at=datetime.now())

        return not registration.save()