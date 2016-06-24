from datetime import datetime,timedelta
from repositories import PaymentDocumentRepository
from repositories.TicketRepository import TicketRepository
from repositories.InvoiceRepository import InvoiceRepository
from

class PaymentService(object):

    __ticket_repository = TicketRepository()
    __invoice_repository = InvoiceRepository()

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

    def payTicket(products, membership_type):

        subtotal = 0
        total_discount = 0
        igv_amount = 0

        for product in products:
            discount = self.getProductDiscount(product)
            subtotal += product['price']
            total_discount += discount

        total = subtotal - discounts + igv_amount

        insert_data = {
            'products': products,
            'subtotal': subtotal,
            'discounts': total_discount,
            'igv_amount': igv_amount,
            'total': total,
            'created_at': datetime.now()
        }

        return  self.__ticket_repository.create(insert_data)

    def payInvoice(products, user_info):
        insert_data = {}
        new_invoice = self.__invoice_repository.create(insert_data)

    def getProductDiscount(product, membership_type):


        return discount