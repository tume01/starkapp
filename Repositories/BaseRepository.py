from contracts.respositories import AbstractBaseRepository

class BaseRepository(metaclass=AbstractBaseRepository):
    def __init__(self, model):
        self.setUpModel(model)

    def setUpModel(self, model):
        __model = model

    def all(self):
        return __model.all()

    def find(self, id):
        return __model.find(id)

    def create(self, create_data):
        return __model.insert(create_data)

    def update(self, update_data):
        return __model.update(update_data)

    def delete(self, id):
        return __model.delete(id)

