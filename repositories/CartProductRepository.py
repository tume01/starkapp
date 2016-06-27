from payment_documents.models import CartProduct
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository

class CartProductRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, CartProduct)
