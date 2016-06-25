from repositories import MembersRepository

class MembersService(object):

    """docstring for MembersService"""

    __member_repository = MembersRepository.MembersRepository()

    def create(self, insert_data):
        return self.__member_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__member_repository.update(id, update_data)

    def delete(self, id):
        return self.__member_repository.delete(id)

    def getMembers(self):
        return self.__member_repository.all()

    def getMember(self,id):
        return self.__member_repository.find(id)

    def filter(self, filters):
        return self.__member_repository.filter(filters)

    def getMemberByUser(self, user):
        filter_data = {}
        filter_data['user'] = user
        return self.__member_repository.filter(filter_data)[0]

    def getUserEvents(self, user):

        member = self.__member_repository.filter({'user': user})[0]

        return member.eventregistration_set.filter(deleted_at=None)