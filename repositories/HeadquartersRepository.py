from headquarters.models import Headquarter
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class HeadquartersRepository(BaseRepository):
	def __init__():
		BaseRepository.__init__(self, Headquarter)