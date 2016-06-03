from bungalow_reservation.models import BungalowReservation
from repositories.BaseRepository import BaseRepository 

class BungalowReservationRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, BungalowReservation) 

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
        return cls._repository.delete(id)

    @classmethod
    def getReservations(cls):
        return cls._repository.all()

    @classmethod
    def findReservation(cls, id):
        return cls._repository.find(id)