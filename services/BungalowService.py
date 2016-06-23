from repositories.BungalowRepository import BungalowRepository

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
        return cls._repository.softDelete(id)

    @classmethod
    def getBungalows(cls):
        return cls._repository.allNotDeleted()

    @classmethod
    def findBungalow(cls, id):
        return cls._repository.find(id)