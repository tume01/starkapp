from headquarters.models import Headquarters
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class HeadquartersRepository(BaseRepository):
	def __init__(self):
		BaseRepository.__init__(self, Headquarters)