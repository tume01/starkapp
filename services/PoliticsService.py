from repositories import PoliticsRepository

class PoliticsService(object):

    """docstring for PoliticsService"""

    __politic_repository = PoliticsRepository.PoliticsRepository()

    def create(self, insert_data):
        return self.__politic_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__politic_repository.update(id, update_data)

    def delete(self, id):
        return self.__politic_repository.softDelete(id)

    def filter(self, filters):
        return self.__politic_repository.filter(filters)

    def getPolitics(self):
        return self.filter({'deleted_at__exact': None})

    def find(self, id):
        return self.__politic_repository.find(id)