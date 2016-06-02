from repositories import ProductsRepository

class ProductsService(object):

    __product_repository = ProductsRepository.ProductsRepository()

    def create(self, insert_data):
        return self.__product_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__product_repository.update(id, update_data)

    def delete(self, id):
        return self.__product_repository.delete(id)

    def getProducts(self):
        return self.__product_repository.all()

    def find(self,id):
        return self.__product_repository.find(id)

    def filter(self, filters):
        return self.__product_repository.filter(filters)