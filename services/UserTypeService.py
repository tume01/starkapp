from repositories import UserTypeRepository

class UsersTypeService(object):

    """docstring for UserTypeService"""

    __user_type_repository = UserTypeRepository.UserTypeRepository()

    def create(self, insert_data):
        return self.__user_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__user_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__user_type_repository.delete(id)

    def getTypes(self):
        return self.__user_type_repository.all()

    def getType(self, id):
        return self.__user_type_repository.find(id)
