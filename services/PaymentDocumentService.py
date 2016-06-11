from repositories import PaymentDocumentRepository

class PaymentDocumentService(object):

    __paymentDocument_repository = PaymentDocumentRepository.PaymentDocumentRepository()

    def create(self, insert_data):
        return self.__paymentDocument_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__paymentDocument_repository.update(id, update_data)

    def delete(self, id):
        return self.__paymentDocument_repository.delete(id)

    def getPaymentDocuments(self):
        return self.__paymentDocument_repository.all()

    def getPaymentDocument(self, id):
        return self.__paymentDocument_repository.find(id)
