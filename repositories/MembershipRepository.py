from memberships.models import Membership
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class MembershipRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Membership)

    def all(self):
        return self.model.objects.filter(status=1)