from environment.models import Environment
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository


class EnvironmentRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, Environment)


