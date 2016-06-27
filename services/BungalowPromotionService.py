from repositories import BungalowPromotionRepository

class BungalowPromotionService(object):

	__bungalow_promotion_repository = BungalowPromotionRepository.BungalowPromotionRepository()

	def create(self, insert_data):
		return self.__bungalow_promotion_repository.create(insert_data)

	def update(self, id, update_data):
		return self.__bungalow_promotion_repository.update(id, update_data)

	def delete(self, id):
		return self.__bungalow_promotion_repository.delete(id)

	def getBungalowPromotion(self):
		return self.__bungalow_promotion_repository.all()

	def findBungalowPromotion(self, id):
		return self.__bungalow_promotion_repository.find(id)
	
	def filter(self, filters):
		return self.__bungalow_promotion_repository.filter(filters)