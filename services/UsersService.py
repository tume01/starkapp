from repositories import UsersRepository

class UsersService(object):

    """docstring for UsersService"""

    __user_repository = UsersRepository.UsersRepository()

    def create(self, insert_data):
        return self.__user_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__user_repository.update(id, update_data)

    def delete(self, id):
        return self.__user_repository.delete(id)

    def getUsers(self):
        return self.__user_repository.all()

    def validateUser(self, id, password):
        user = self.__user_repository.find(id)
        if (user == None):
            return None
        if (user.password != password):
            return None        
        return user.UserType
