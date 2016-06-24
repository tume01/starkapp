from suspension.models import SuspensionType
from .BaseRepository import BaseRepository

class SuspensionTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, SuspensionType)