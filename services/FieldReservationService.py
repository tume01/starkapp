from repositories import FieldReservationRepository
import datetime, calendar, time,collections

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
    def getDayAvailableHours(cls, courts,courtHeadquarterId, courtTypeId, start,end):
        startDate = datetime.datetime.fromtimestamp(start)
        endDate = datetime.datetime.fromtimestamp(end)
        num_days = (endDate - startDate).days + 1
        days = [startDate + datetime.timedelta(days=delta) for delta in range(0,num_days)]

        reservations = this.getReservations()

        reservations = reservations.filter(reservation_date=startDate)

        if (headquarter_id != -1):

            print("Filter by Headquarter_ID")
            reservations = reservations.filter(headquarter_id=courtHeadquarterId)

        if (court_type_id != -1):

            print("Filter by court_type_id")
            reservations = reservations.filter(court_type=courtTypeId)


        reservations_list= []
        for r in reservations:
            hours = r.reservation_duration
            while hours < 0:
                reservations_list += r.reservation_hour + datetime.timedelta(hours=hours)
                hours -= 1

        ocurrences = collections.Counter(reservations_list)

        date = [(day,courts.count() - ocurrences[int(day.strftime("%Y%m%d%H%M%S"))]) for day in days]

        availableDays = [{
            'title': str(day[1]) + 'Canchas disponibles',
            'start': day[0].strftime("%Y-%m-%dT%H:%M:%S"),
        } for day in date if (day[1] != 0)]

        print(availableDays)

        return availableDays

