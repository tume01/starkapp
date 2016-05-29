from repositories import EntryRepository

class EntryService(object):

    __entry_repository = EntryRepository.EntryRepository()

    def create(self, insert_data):
        return self.__entry_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__entry_repository.update(id, update_data)

    def delete(self, id):
        return self.__entry_repository.delete(id)

    def getEntries(self):
        return self.__entry_repository.all()

    def getEntry(self, id):
        return self.__entry_repository.find(id)
