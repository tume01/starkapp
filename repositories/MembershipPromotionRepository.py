from promotions.models import MembershipPromotion
from repositories.BaseRepository import BaseRepository 

class MembershipPromotion(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, MembershipPromotion) 
