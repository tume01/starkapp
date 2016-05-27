from repositories import BungalowTypeRepository as repo

class BungalowTypeService(object):

    """docstring for BungalowTypeService"""

    _repository = repo.BungalowTypeRepository()
    
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
    def findBungalowType(cls, id):
        return cls._repository.find(id)