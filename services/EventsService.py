from repositories import EventsRepository

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