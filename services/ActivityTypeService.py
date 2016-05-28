from repositories.ActivityTypeRepository import ActivityTypeRepository

class ActivityTypeService(object):

    """docstring for ActivityService"""

    __activity_type_repository = ActivityTypeRepository()

    def create(self, insert_data):
        return self.__activity_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__activity_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__activity_type_repository.delete(id)

    def getActivityTypes(self):
        return self.__activity_type_repository.all()

    def filter(self, filters):
        return self.__activity_type_repository.filter(filters)

    def getActivityType(self, id):
        return self.__activity_type_repository.find(id)