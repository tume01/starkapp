from repositories import SuspensionTypeRepository

class SuspensionTypeService(object):

    """docstring for FineService"""

    __suspension_type_repository = SuspensionTypeRepository.SuspensionTypeRepository()

    def create(self, insert_data):
        return self.__suspension_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__suspension_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__suspension_type_repository.delete(id)

    def getSuspensionTypes(self):
        return self.__suspension_type_repository.all()

    def getSuspensionType(self, id):
        return self.__suspension_type_repository.find(id)
