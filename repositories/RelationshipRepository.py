from affiliate.models import Relationship
from .BaseRepository import BaseRepository

class RelationshipRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Relationship)

    def all(self):
        return self.model.objects.all()