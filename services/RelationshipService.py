from repositories import RelationshipRepository

class RelationshipService(object):

	__relationship_repository = RelationshipRepository.RelationshipRepository()

	def create(self, insert_data):
		return self.__relationship_repository.create(insert_data)

	def update(self, id, update_data):
		return self.__relationship_repository.update(id, update_data)

	def delete(self, id):
		return self.__relationship_repository.delete(id)

	def getRelationships(self):
		return self.__relationship_repository.all()

	def getRelationship(self, id):
		return self.__relationship_repository.find(id)

	def filter(self, filters):
		return self.__relationship_repository.filter(filters)