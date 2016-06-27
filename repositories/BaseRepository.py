from django.core.exceptions import ObjectDoesNotExist
from contracts.repositories.AbstractBaseRepository import AbstractBaseRepository
import datetime

class BaseRepository(AbstractBaseRepository):

    model = None

    def __init__(self, model):
        self.setUpModel(model)

    def setUpModel(self, model):
        self.model = model

    def all(self):
        return self.model.objects.all()

    def allNotDeleted(self):
        return self.filter({"deleted_at" : None})

    def find(self, find_id):
        try:
            return self.model.objects.get(id=find_id)
        except ObjectDoesNotExist:
            return None

    def create(self, create_data):
        new_element = self.model(**create_data)

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

    def softDelete(self, delete_id):
        return self.update(delete_id,{"deleted_at": datetime.datetime.now()})

    def filter(self, filters):
        return self.model.objects.filter(**filters)

    def distinct(self, value):
        return self.model.objects.values(value).distinct()

    def distinctFilter(self, value, filters):
        return self.model.objects.filter(**filters).values(value).distinct()


