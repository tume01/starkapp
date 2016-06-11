from repositories import SuspensionRepository

class SuspensionService(object):

    """docstring for PromotionssService"""

    __suspension_repository = SuspensionRepository.SuspensionRepository()

    def create(self, insert_data):
        return self.__suspension_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__suspension_repository.update(id, update_data)

    def getSuspensions(self):
        return self.__suspension_repository.all()

    def getSuspension(self, id):
        return self.__suspension_repository.find(id)

    def filter(self,filters):
        return self.__suspension_repository.filter(filters)

