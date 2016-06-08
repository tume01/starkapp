from repositories import EnvironmentRepository
from repositories import EnvironmentReservationRepository

class EnvironmentService(object):

    """docstring for EnvironmentService"""

    __environment_repository = EnvironmentRepository.EnvironmentRepository()
    __environment_reservation_repository = EnvironmentReservationRepository.EnvironmentReservationRepository()

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

    def getEnvironmentByStatus(self):
        return self.__environment_repository.getActiveEnvironment()

    def filter(self, filters):
        return self.__environment_repository.filter(filters)

    def filterReservations(self, filters):
        return self.__environment_reservation_repository.filter(filters)

    def createReservation(self, insert_data):
        return self.__environment_reservation_repository.create(insert_data)