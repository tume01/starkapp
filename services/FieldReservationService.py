from repositories import FieldReservationRepository

class FieldReservationService(object):

    """docstring for BungalowsService"""

    __field_reservation_repository = FieldReservationRepository.FieldReservationRepository()

    def create(self, insert_data):
        return self.__field_reservation_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__field_reservation_repository.update(id, update_data)

    def delete(self, id):
        return self.__field_reservation_repository.delete(id)

    def getReservations(self):
        return self.__field_reservation_repository.all()

    def filter(self,filters):
        return self.__field_reservation_repository.filter(filters)
