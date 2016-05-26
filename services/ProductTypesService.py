from repositories import ProductTypesRepository

class ProductTypesService(object):

    __product_type_repository = ProductTypesRepository.ProductTypesRepository()

    def create(self, insert_data):
        return self.__product_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__product_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__product_type_repository.delete(id)

    def getProductTypes(self):
        return self.__product_type_repository.all()

    def find(self,id):
        return self.__product_type_repository.find(id)