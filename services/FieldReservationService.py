from repositories import FieldReservationRepository
import datetime, calendar, time

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

    @classmethod
    def getDayAvailableHours(cls, bungalowTypeId, month, year):

        num_days = calendar.monthrange(year, month)[1]
        days = [datetime.date(year, month, day,hour) for day in range(1, num_days + 1)]

        #hours = [(i, datetime.time(i).strftime('%I %p')) for i in range(24)]

        for day in days:
            availableDays = {
                'title': 'Disponible',
                'start': day.strftime("%Y-%m-%dT%H:%M:%S")
            } 

        print(availableDays)

        return availableDays
