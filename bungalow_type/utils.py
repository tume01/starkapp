from bungalow_type.models import BungalowType
from repositories.BaseRepository import BaseRepository

class BungalowTypeRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, BungalowType)


class BungalowTypeService(object):
    """docstring for BungalowTypeService"""

    _repository = BungalowTypeRepository()
    
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
    def getBungalowTypes(cls):
        return cls._repository.all()

    @classmethod
    def findBungalowType(cls, id):
        return cls._repository.find(id)