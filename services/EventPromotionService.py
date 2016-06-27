from repositories import EventPromotionRepository

class EventPromotionService(object):

	__event_promotion_repository = EventPromotionRepository.EventPromotionRepository()

	def create(self, insert_data):
		return self.__event_promotion_repository.create(insert_data)

	def update(self, id, update_data):
		return self.__event_promotion_repository.update(id, update_data)

	def delete(self, id):
		return self.__event_promotion_repository.delete(id)

	def getEventPromotion(self):
		return self.__event_promotion_repository.all()

	def findEventPromotion(self, id):
		return self.__event_promotion_repository.find(id)
	
	def filter(self, filters):
		return self.__event_promotion_repository.filter(filters)