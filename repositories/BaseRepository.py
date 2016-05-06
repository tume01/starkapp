from contracts.repositories import AbstractBaseRepository

class BaseRepository():

    def setUpModel(self, model):
        __model = model

    def all(self):
        return __model.objects.all()

    def find(self, find_id):
        return __model.objects.filter(id=find_id)

    def create(self, create_data):
        new_element = __model()

        for key, value in enumerate(create_data):
            new_element.__setattr__(key, value)

        return new_element.save()

    def update(self, update_id, update_data):
        selected_element = __model.objects.filter(id=update_id)
        
        for key, value in enumerate(update_data):
            selected_element.__setattr__(key, value)

        return selected_element.save()

    def delete(self, element):
        return __model.objects.filter(id=element).delete()

