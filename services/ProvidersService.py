from repositories import ProvidersRepository

class ProvidersService(object):

    """docstring for ProvidersService"""

    __provider_repository = ProvidersRepository.ProvidersRepository()

    def create(self, insert_data):
        return self.__provider_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__provider_repository.update(id, update_data)

    def delete(self, id):
        return self.__provider_repository.delete(id)

    def getProviders(self):
        return self.__provider_repository.all()

    def getActiveProviders(self):
        return self.__provider_repository.getActiveProviders()

    def find(self,id):
        return self.__provider_repository.find(id)