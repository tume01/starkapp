from repositories import ActivityRepository

class ActivityService(object):

    """docstring for ActivityService"""

    __activity_repository = ActivityRepository.ActivityRepository()

    def create(self, insert_data):
        return self.__activity_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__activity_repository.update(id, update_data)

    def delete(self, id):
        return self.__activity_repository.delete(id)

    def getBungalows(self):
        return self.__activity_repository.all()

    def filter(self, filters):
        return self.__activity_repository.filter(filters)