from repositories import HeadquartersRepository

class HeadquarterService(object):

	__headquarters_repository = HeadquartersRepository.HeadquartersRepository()

	def create(self, insert_data):
		return self.__headquarters_repository.create(insert_data)

	def update(self, id, update_data):
		return self.__headquarters_repository.update(id, update_data)

	def delete(self, id):
		return self.__headquarters_repository.delete(id)

	def getHeadquarters(self):
		return self.__headquarters_repository.all()

	def findHearquarter(self, id):
		return self.__headquarters_repository.findHearquarter(id)