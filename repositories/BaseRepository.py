from contracts.repositories.AbstractBaseRepository import AbstractBaseRepository

class BaseRepository(AbstractBaseRepository):

    __model = None

    def __init__(self, model):
        self.setUpModel(model)

    def setUpModel(self, model):
        self.__model = model

    def all(self):
        return self.__model.objects.all()

    def find(self, find_id):
        return self.__model.objects.get(id=find_id)

    def create(self, create_data):
        new_element = self.__model()

        for key, value in create_data.items():
            new_element.__setattr__(key, value)

        return new_element.save()

    def update(self, update_id, update_data):
        selected_element = self.__model.objects.filter(id=update_id)
        
        for key, value in update_data.items():
            selected_element.__setattr__(key, value)

        return selected_element.save()

    def delete(self, element):
        return self.__model.objects.filter(id=element).delete()