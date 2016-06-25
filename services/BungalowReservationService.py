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
    def getMonthAvailableDaysBF(cls, bungalowHeadquarterId, bungalowTypeId, start, end):
        startDate = datetime.datetime.fromtimestamp(start)
        endDate = datetime.datetime.fromtimestamp(end)
        num_days = (endDate - startDate).days + 1
        days = [startDate + datetime.timedelta(days=delta) for delta in range(0, num_days)]

        reservations = cls.getReservations()
        reservations = reservations.filter(departure_date__gte=startDate, arrival_date__lte=endDate)
        bungalows = BungalowService.getBungalows()

        if (bungalowTypeId != -1):
            print("Filter by Type_ID")
            reservations = reservations.filter(bungalow_type_id=bungalowTypeId)
            bungalows = bungalows.filter(bungalow_type__id=bungalowTypeId)

        if (bungalowHeadquarterId != -1):
            print("Filter by Headquarter_ID")
            reservations = reservations.filter(bungalow_headquarter_id=bungalowHeadquarterId)
            bungalows = bungalows.filter(headquarter__id=bungalowHeadquarterId)

            # Get list of reserved bungalows (day, #reservations)
            # print([(r.bungalow_id,r.bungalow_headquarter.id) for r in reservations])
        print(reservations)
        bungalowDay = []
        # for each Bungalow
        for day in days:
            # List of bungalows available this day
            aBungDay = []
            for bungalow in bungalows:
                reservationsPerBungalow = reservations.filter(bungalow_id=bungalow.id)
                flag = True
                for reservation in reservationsPerBungalow:
                    if int(day.strftime('%Y%m%d')) in reservation.getReservationDays():
                        flag = False
                        pass
                    pass
                if (flag):
                    aBungDay.append((day.strftime('%Y%m%d'), bungalow.id))
                pass
            bungalowDay.append(aBungDay)
            pass

        print(days)
        print(bungalowDay)
        print(len(days))
        print(len(bungalowDay))

        # Compose the url (Worst Approach EVER!)
        url = "create/reserve/?bungalow_id={}&date={}";

        returnValue = []
        for n in range(len(bungalowDay)):
            day = bungalowDay[n]
            for bday in day:
                element = {'title': 'Bungalow ' + str(bday[1]),
                           'start': days[n].isoformat(),
                           'url': url.format(str(bday[1]), str(int(days[n].timestamp())))
                           }
                returnValue.append(element)

        print(returnValue)
        return returnValue
    #
    # @classmethod
    # def getMonthAvailableDays(cls, bungalowHeadquarterId, bungalowTypeId, start, end):
    #     startDate = datetime.datetime.fromtimestamp(start)
    #     endDate = datetime.datetime.fromtimestamp(end)
    #     num_days = (endDate - startDate).days + 1
    #     days = [startDate + datetime.timedelta(days=delta) for delta in range(0, num_days)]
    #
    #     reservations = cls.getReservations()
    #     reservations = reservations.filter(departure_date__gte=startDate, arrival_date__lte=endDate)
    #     bungalows = BungalowService.getBungalows()
    #
    #     if (bungalowTypeId != -1):
    #         print("Filter by Type_ID")
    #         reservations = reservations.filter(bungalow_type_id=bungalowTypeId)
    #         bungalows = bungalows.filter(bungalow_type__id=bungalowTypeId)
    #
    #     if (bungalowHeadquarterId != -1):
    #         print("Filter by Headquarter_ID")
    #         reservations = reservations.filter(bungalow_headquarter_id=bungalowHeadquarterId)
    #         bungalows = bungalows.filter(headquarter__id=bungalowHeadquarterId)
    #
    #     # Get list of reserved bungalows (day, #reservations)
    #     # print([(r.bungalow_id,r.bungalow_headquarter.id) for r in reservations])
    #
    #     reservationList = []
    #     for r in reservations:
    #         reservationList += r.getReservationDays()
    #     ocurrences = collections.Counter(reservationList)
    #
    #     print(int(startDate.strftime('%Y%m%d')), int(endDate.strftime('%Y%m%d')))
    #     print(ocurrences)
    #     print(days)
    #     # print([(int(day.strftime('%Y%m%d')),bungalows.count() - ocurrences[int(day.strftime('%Y%m%d'))]) for day in days])
    #
    #     days = [(day, bungalows.count() - ocurrences[int(day.strftime('%Y%m%d'))]) for day in days]
    #
    #     # Compose the url (Worst Approach EVER!)
    #     url = "create/reserve/?";
    #     url += "bungalow_type_id=" + str(bungalowTypeId) + "&"
    #     url += "headquarter_id=" + str(bungalowHeadquarterId) + "&"
    #     url += "date="
    #
    #     return [{'title': str(day[1]) + ' Bungalows Disponibles',
    #              'start': day[0].isoformat(),
    #              'url': url + str(int(day[0].timestamp()))
    #              } for day in days if (day[1] != 0)]

    @classmethod
    def getReservationsByMember(cls, member_id):
        filter_data = {}
        filter_data['member_id'] = member_id
        filter_data['status'] = 2 #reservation in use
        return cls._repository.filter(filter_data)

    @classmethod
    def getReservationsByBungalow(cls, bungalow_id):
        filter_data = {}
        filter_data['bungalow_id'] = bungalow_id
        filter_data['status'] = 2 #reservation in use
        return cls._repository.filter(filter_data)
