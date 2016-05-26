from repositories import HeadquartersRepository

class HeadqueartesService(object):

	__headquarters_repository = HeadquartersRepository.HeadquartersRepository()

	def create(self, insert_data):
		return self.__headquarters_repository.create(insert_data)

	def update(self, id, update_data):
		return self.__headquarters_repository.update(id, update_data)

	def delete(self, id):
		return self.__headquarters_repository.delete(id)

	def getHeadquarter(self, id):
		return self.__headquarters_repository.getHeadquarter(id)

	def findHearquarter(self, id):
		return self.__headquarters_repository.findHearquarter(id)