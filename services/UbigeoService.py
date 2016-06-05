from repositories import UbigeoRepository

class UbigeoService(object):

    __ubigeo_repository = UbigeoRepository.UbigeoRepository()

    def create(self, insert_data):
        return self.__ubigeo_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__ubigeo_repository.update(id, update_data)

    def delete(self, id):
        return self.__ubigeo_repository.delete(id)

    def getAllUbigeo(self):
        return self.__ubigeo_repository.all()

    def getUbigeoById(self, id):
        return self.__ubigeo_repository.find(id)

    def filter(self, filters):
        return self.__ubigeo_repository.filter(filters)