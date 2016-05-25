from contracts.repositories.AbstractBaseRepository import AbstractBaseRepository

class BaseRepository(AbstractBaseRepository):

    model = None

    def __init__(self, model):
        self.setUpModel(model)

    def setUpModel(self, model):
        self.model = model

    def all(self):
        return self.model.objects.all()

    def find(self, find_id):
        return self.model.objects.get(id=find_id)

    def create(self, create_data):
        new_element = self.model()

        for key, value in create_data.items():
            new_element.__setattr__(key, value)

        new_element.save()

        return new_element

    def update(self, update_id, update_data):
        selected_element = self.model.objects.get(id=update_id)
        
        for key, value in update_data.items():
            selected_element.__setattr__(key, value)

        selected_element.save()

        return selected_element

    def delete(self, element):
        return self.model.objects.get(id=element).delete()

    def filter(self, filters):
        return self.model.objects.filter(**filters)
