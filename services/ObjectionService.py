from repositories import ObjectionsRepository

class ObjectionsService(object):

    """docstring for ObjectionService"""

    __objection_repository = ObjectionsRepository.ObjectionsRepository()

    def create(self, insert_data):
        return self.__objection_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__objection_repository.update(id, update_data)

    def delete(self, id):
        return self.__objection_repository.delete(id)

    def getObjection(self, id):
        return self.__objection_repository.find(id)

    def getObjections(self, id):
        return self.__objection_repository.all()

    def getObjectionByApplicationId(self, id):
        filter_objection = {}
        filter_objection['membership_application'] = id
        return self.__objection_repository.filter(filter_objection)
