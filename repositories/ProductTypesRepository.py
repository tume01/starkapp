from products.models import ProductType
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class ProductTypesRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, ProductType)