from repositories import PromotionsRepository

class PromotionService(object):

    """docstring for PromotionssService"""

    __promotion_repository = PromotionsRepository.PromotionsRepository()

    def create(self, insert_data):
        return self.__promotion_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__promotion_repository.update(id, update_data)

    def delete(self, id):
        return self.__promotion_repository.delete(id)

    def getPromotions(self):
        return self.__promotion_repository.all()

    def getPromotion(self, id):
        return self.__promotion_repository.find(id)
