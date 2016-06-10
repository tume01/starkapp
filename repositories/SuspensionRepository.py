from suspension.models import Suspension
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class SuspensionRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Suspension)