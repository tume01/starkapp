
from providers.models import Provider
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 


class ProvidersRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Provider)

    def getActiveProviders(self):
        return self.model.objects.filter(status=1) #status 1 means active


