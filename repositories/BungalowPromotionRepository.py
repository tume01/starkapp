from promotions.models import BungalowReservationPromotion
from repositories.BaseRepository import BaseRepository

class BungalowPromotionRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, BungalowReservationPromotion)

