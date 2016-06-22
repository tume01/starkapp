from environment.models 	import EnvironmentType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository 		import BaseRepository 

class EnvironmentTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, EnvironmentType)

