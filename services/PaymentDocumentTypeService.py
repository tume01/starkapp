from repositories import PaymentDocumentTypeRepository

class PaymentDocumentTypeService(object):

    __paymentDocument_type_repository = PaymentDocumentTypeRepository.PaymentDocumentTypeRepository

    def create(self, insert_data):
        return self.__paymentDocument_type_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__paymentDocument_type_repository.update(id, update_data)

    def delete(self, id):
        return self.__paymentDocument_type_repository.delete(id)

    def getDocumentTypes(self):
        return self.__paymentDocument_type_repository.all()

    def getDocumentType(self, id):
        return self.__paymentDocument_type_repository.find(id)
