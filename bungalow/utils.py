from bungalow.models import Bungalow
from repositories.BaseRepository import BaseRepository 

class BungalowRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, Bungalow) 

class BungalowService(object):
    """docstring for BungalowsService"""

    _repository = BungalowRepository()

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
    def getBungalows(cls):
        return cls._repository.all()

    @classmethod
    def findBungalow(cls, id):
        return cls._repository.find(id)

    @classmethod
    def filterBungalows(cls, **filters):
        return cls._repository.filter(**filters)