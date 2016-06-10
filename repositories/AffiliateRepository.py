from affiliate.models import Affiliate
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class AffiliateRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Affiliate)

    
    def all(self):
        return self.model.objects.filter(state=1)
