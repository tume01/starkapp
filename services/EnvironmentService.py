from repositories import EnvironmentRepository

class EnvironmentService(object):

    """docstring for BungalowsService"""

    __environment_repository = EnvironmentRepository.EnvironmentRepository()

    def create(self, insert_data):
        return self.__environment_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__environment_repository.update(id, update_data)

    def delete(self, id):
        return self.__environment_repository.delete(id)

    def getEnvironment(self):
        return self.__environment_repository.all()

    def getEnviromentById(self, environment_id):
        return self.__environment_repository.find(environment_id)