from repositories.BungalowReservationRepository import BungalowReservationRepository
import datetime, calendar, time

class BungalowReservationService(object):
    """docstring for BungalowsService"""

    _repository = BungalowReservationRepository()

    @classmethod
    def create(cls, insert_data):
        return cls._repository.create(insert_data)

    @classmethod
    def update(cls, id, update_data):
        return cls._repository.update(id, update_data)

    @classmethod
    def delete(cls, id):
        return cls._repository.softDelete(id)

    @classmethod
    def getReservations(cls):
        return cls._repository.allNotDeleted()

    @classmethod
    def findReservation(cls, id):
        return cls._repository.find(id)

    @classmethod
    def getMonthAvailableDays(cls, bungalowTypeId, month, year):

        num_days = calendar.monthrange(year, month)[1]
        days = [datetime.date(year, month, day) for day in range(1, num_days + 1)]

        availableDays = [{
            'title': 'Disponible',
            'start': day.isoformat()
        } for day in days]

        print(availableDays)

        return availableDays
