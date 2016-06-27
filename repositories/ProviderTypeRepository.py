from providers.models import ProviderType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class ProviderTypesRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, ProviderType)