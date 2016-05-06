from contracts.repositories import AbstractBungalowsRepository
from bungalows.models import Bungalow

class BungalowsRepository(base_repository=BaseRepository, metaclass=AbstractBungalowsRepository):

    def __init__(self):
        self.setUpModel(Bungalow)

