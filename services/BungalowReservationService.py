from repositories.BungalowReservationRepository import BungalowReservationRepository
import datetime, calendar, collections
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

        reservations = reservations \
            .filter(departure_date__gte=startDate, arrival_date__lte=endDate)
            # .filter(bungalow_type_id=bungalowTypeId) \
            # .filter(bungalow_headquarter_id=bungalowHeadquarterId)
        #

        # Get bungalow count
        bungalowsTotal = BungalowService.getBungalows().count()

        # Get list of reserved bungalows (day, #reservations)
        reservationList = []
        for r in reservations:
            reservationList += r.getReservationDays()
        ocurrences = collections.Counter(reservationList)

        days = [(day, bungalowsTotal - ocurrences[int(day.strftime('%Y%m%d'))]) for day in days]

        availableDays = [{
                             'title': str(day[1]) + ' Bungalows Disponibles' if (day[1] != 0) else "No disponible",
                             'start': day[0].isoformat()
                         } for day in days ]

        return availableDays
