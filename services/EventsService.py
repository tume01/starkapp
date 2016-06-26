from repositories import EventsRepository
from datetime import datetime,date,timedelta

class EventsService(object):

    """docstring for BungalowsService"""

    __event_repository = EventsRepository.EventsRepository()

    def create(self, insert_data):
        return self.__event_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__event_repository.update(id, update_data)

    def delete(self, id):
        return self.__event_repository.delete(id)

    def getEvents(self):
        return self.__event_repository.all()

    def filter(self,filters):
        return self.__event_repository.filter(filters)

    def getEvent(self, id):
        return self.__event_repository.find(id)

    def registerMember(self, event_id, user, guests):

        event = self.getEvent(event_id)

        assistants = event.eventregistration_set.filter(deleted_at=None).count()

        if event.assistance > assistants:

            if not event.eventregistration_set.filter(member_id=user.id, deleted_at=None):
                return self.__event_repository.addMember(event, user, guests)

        return None

    def removeUserRegistration(self, event_id, member_id):
        event = self.getEvent(event_id)

        week_before = date.today() - timedelta(days=7)
      
        return event.eventregistration_set.filter(member_id=member_id, registered_at__gte=week_before).update(deleted_at=datetime.now())

    def getEventRegistrations(self, event_id):

        event = self.getEvent(event_id)

        return event.eventregistration_set.filter(deleted_at=None)

    @classmethod
    def get(cls, id):
        return cls.__event_repository.find(id)