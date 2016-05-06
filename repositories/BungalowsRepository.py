from . import BaseRepository
from contracts.repositories import AbstractBungalowsRepository
from bungalows.models import Bungalow

class BungalowsRepository():

    __model = None

    def __init__(self):
        self.setUpModel(Bungalow)

    def setUpModel(self, model):
        self.__model = model

    def all(self):
        return self.__model.objects.all()

    def find(self, find_id):
        return self.__model.objects.filter(id=find_id)

    def create(self, create_data):
        new_element = self.__model()

        for key, value in enumerate(create_data):
            new_element.__setattr__(key, value)

        return new_element.save()

    def update(self, update_id, update_data):
        selected_element = self.__model.objects.filter(id=update_id)
        
        for key, value in enumerate(update_data):
            selected_element.__setattr__(key, value)

        return selected_element.save()

    def delete(self, element):
        return self.__model.objects.filter(id=element).delete()