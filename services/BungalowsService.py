from repositories import BungalowsRepository

class BungalowsService(object):

    """docstring for BungalowsService"""

    __bungalow_repository = BungalowsRepository.BungalowsRepository()

    def create(self, insert_data):
        return self.__bungalow_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__bungalow_repository.update(id, update_data)

    def delete(self, id):
        return self.__bungalow_repository.delete(id)

    def getBungalows(self):
        return self.__bungalow_repository.all()