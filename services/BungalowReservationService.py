from repositories.BungalowReservationRepository import BungalowReservationRepository
import datetime, calendar
from services.BungalowService import BungalowService


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
    def getMonthAvailableDays(cls, bungalowHeadquarterId, bungalowTypeId, start, end):
        startDate = datetime.datetime.fromtimestamp(start)
        endDate = datetime.datetime.fromtimestamp(end)
        num_days = (endDate - startDate).days
        days = [startDate + datetime.timedelta(days=delta) for delta in range(0, num_days)]

        reservations = cls.getReservations();

        # reservations = reservations \
        #     .filter(bungalow_type_id=bungalowTypeId) \
        #     .filter(bungalow_headquarter_id=bungalowHeadquarterId)
        #
        # reservationList = []
        # for r in reservations:
        #     reservationList += r.getReservationDays()
        #
        # bungalows = BungalowService.getBungalows().count()
        #
        # for day in days:
        #     flag = False
        #     for r in reservations:
        #         pass

        availableDays = [{
                             'title': 'Disponible',
                             'start': day.isoformat()
                         } for day in days]

        print(availableDays)

        return availableDays
