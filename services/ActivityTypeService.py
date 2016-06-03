from repositories.ActivityTypeRepository import ActivityTypeRepository

class ActivityTypeService(object):

    """docstring for ActivityService"""

    __activity_type_repository = ActivityTypeRepository()

    @classmethod
    def create(self, insert_data):
        return self.__activity_type_repository.create(insert_data)

    @classmethod
    def update(self, id, update_data):
        return self.__activity_type_repository.update(id, update_data)

    @classmethod
    def delete(self, id):
        return self.__activity_type_repository.delete(id)

    @classmethod
    def getActivityTypes(self):
        return self.__activity_type_repository.all()

    @classmethod
    def filter(self, filters):
        return self.__activity_type_repository.filter(filters)

    @classmethod
    def getActivityType(self, id):
        return self.__activity_type_repository.find(id)