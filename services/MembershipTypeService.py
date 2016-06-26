from repositories import MembershipTypeRepository

class MembershipTypeService(object):

    """docstring for MembershipTypeService"""

    __membership_type_repository = MembershipTypeRepository.MembershipTypeRepository()

    def create(self, insert_data):
        return self.__membership_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__membership_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__membership_type_repository.delete(id)

    def getMembershipTypes(self):
        return self.__membership_type_repository.all()

    def getType(self, id):
        return self.__membership_type_repository.find(id)

    def filter(self, filters):
        return self.__membership_type_repository.filter(filters)
