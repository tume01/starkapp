from repositories import EnvironmentTypeRepository

class EnvironmentTypeService(object):

    """docstring for BungalowsService"""

    __environment_type_repository = EnvironmentTypeRepository.EnvironmentTypeRepository()

    def create(self, insert_data):
        return self.__environment_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__environment_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__environment_type_repository.delete(id)

    def getEnvironment(self):
        return self.__environment_type_repository.all()

    def getEnviromentById(self, environment_id):
        return self.__environment_type_repository.find(environment_id)

    def getEnvironmentByStatus(self):
        return self.__environment_type_repository.getActiveEnvironment()