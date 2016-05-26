from repositories import GuestRepository

class GuestService(object):

    __guest_repository = GuestRepository.GuestRepository()

    def create(self, insert_data):
        return self.__guest_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__guest_repository.update(id, update_data)

    def delete(self, id):
        return self.__guest_repository.delete(id)

    def getGuests(self):
        return self.__guest_repository.all()

    def getGuest(self, id):
        return self.__guest_repository.find(id)
