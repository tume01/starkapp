from repositories import MembershipRepository

class MembershipService(object):

    """docstring for PromotionssService"""

    __membership_repository = MembershipRepository.MembershipRepository()

    def create(self, insert_data):
        return self.__membership_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__membership_repository.update(id, update_data)

    def getMemberships(self):
        return self.__membership_repository.all()

    def getMembership(self, id):
        return self.__membership_repository.find(id)

    def filter(self,filters):
        return self.__membership_repository.filter(filters)

    @classmethod
    def get(cls,id):
        return cls.__membership_repository.find(id)