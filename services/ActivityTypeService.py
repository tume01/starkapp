from repositories.ActivityTypeRepository import ActivityTypeRepository

class ActivityTypeService(object):

    """docstring for ActivityService"""

    __activity_type_repository = ActivityTypeRepository()

    @classmethod
    def create(cls, insert_data):
        return cls.__activity_type_repository.create(insert_data)

    @classmethod
    def update(cls, id, update_data):
        return cls.__activity_type_repository.update(id, update_data)

    @classmethod
    def delete(cls, id):
        return cls.__activity_type_repository.delete(id)

    @classmethod
    def getActivityTypes(cls):
        return cls.__activity_type_repository.all()

    @classmethod
    def filter(cls, filters):
        return cls.__activity_type_repository.filter(filters)

    @classmethod
    def getActivityType(cls, id):
        return cls.__activity_type_repository.find(id)