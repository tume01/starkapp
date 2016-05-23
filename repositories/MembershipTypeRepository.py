from memberships.models import MembershipType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class MembershipTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, MembershipType)

    def all(self):
        return self.model.objects.filter(status=1)
