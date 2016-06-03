from repositories import IdentityDocumentTypeRepository

class IdentityDocumentTypeService(object):

	__identity_document_repository = IdentityDocumentTypeRepository.IdentityDocumentTypeRepository()

	def create(self, insert_data):
		return self.__identity_document_repository.create(insert_data)

	def update(self, id, update_data):
		return self.__identity_document_repository.update(id, update_data)

	def delete(self, id):
		return self.__identity_document_repository.delete(id)

	def getIdentityDocumentTypes(self):
		return self.__identity_document_repository.all()

	def getIdentityDocumentType(self, id):
		return self.__identity_document_repository.find(id)