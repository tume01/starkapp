from repositories import EventsTypeRepository

class EventsTypeService(object):

    """docstring for BungalowsService"""

    __eventsType_repository = EventsTypeRepository.EventsTypeRepository()

    def create(self, insert_data):
        return self.__eventsType_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__eventsType_repository.update(id, update_data)

    def delete(self, id):
        return self.__eventsType_repository.delete(id)

    def getEventsType(self):
        return self.__eventsType_repository.all()

    def filter(self, )