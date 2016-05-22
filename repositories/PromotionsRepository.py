from promotions.models import Promotion
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class PromotionsRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Promotion)
