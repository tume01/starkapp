from repositories import ProviderTypeRepository

class ProviderTypesService(object):

    __provider_type_repository = ProviderTypeRepository.ProviderTypesRepository()

    def create(self, insert_data):
        return self.__provider_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__provider_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__provider_type_repository.delete(id)

    def getProductTypes(self):
        return self.__provider_type_repository.all()

    def find(self,id):
        return self.__provider_type_repository.find(id)