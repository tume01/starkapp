from repositories import Membership_ApplicationRepository

class Membership_ApplicationService(object):

    """docstring for Membership_ApplicationService"""

    __membership_application_repository = Membership_ApplicationRepository.Membership_ApplicationRepository()

    def create(self, insert_data):
        return self.__membership_application_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__membership_application_repository.update(id, update_data)

    def delete(self, id):
        return self.__membership_application_repository.delete(id)

    def getMembership_Applications(self):
        return self.__membership_application_repository.all()

    def getMembership_Application(self,id):
        return self.__membership_application_repository.find(id)

    def filter(self, filters):
        return self.__membership_application_repository.filter(filters)
