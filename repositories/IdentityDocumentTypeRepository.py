from identity_document_type.models import Identity_Document_Type
from .BaseRepository import BaseRepository

class IdentityDocumentTypeRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Identity_Document_Type)

    def all(self):
        return self.model.objects.filter(status=1)