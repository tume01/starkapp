from promotions.models import EventPromotion
from repositories.BaseRepository import BaseRepository 

class EventPromotionRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, EventPromotion) 
