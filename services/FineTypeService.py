from repositories import FineTypeRepository

class FineTypeService(object):

    """docstring for FineService"""

    __fine_type_repository = FineTypeRepository.FineTypeRepository()

    def create(self, insert_data):
        return self.__fine_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__fine_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__fine_type_repository.delete(id)

    def getFines(self):
        return self.__fine_type_repository.all()

    def getFine(self, id):
        return self.__fine_type_repository.find(id)
