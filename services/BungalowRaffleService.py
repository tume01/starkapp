from repositories.BungalowRaffleRepository import BungalowRaffleRepository


class BungalowRaffleService(object):
    """docstring for BungalowRaffleService"""

    _repository = BungalowRaffleRepository()

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
    def getRaffles(cls):
        return cls._repository.allNotDeleted()

    @classmethod
    def findRaffle(cls, id):
        return cls._repository.find(id)
