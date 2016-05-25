from products.models import Product
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class ProductsRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Product)