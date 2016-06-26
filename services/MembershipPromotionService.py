from repositories import MembershipPromotionRepository

class MembershipPromotionService(object):

	__membership_promotion_repository = MembershipPromotionRepository.MembershipPromotion()

	def create(self, insert_data):
		return self.__membership_promotion_repository.create(insert_data)

	def update(self, id, update_data):
		return self.__membership_promotion_repository.update(id, update_data)

	def delete(self, id):
		return self.__membership_promotion_repository.delete(id)

	def getMembershipPromotion(self):
		return self.__membership_promotion_repository.all()

	def findHeadquarter(self, id):
		return self.__membership_promotion_repository.find(id)
	
	def filter(self, filters):
		return self.__membership_promotion_repository.filter(filters)