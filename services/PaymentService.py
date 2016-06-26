from datetime import datetime,timedelta
from repositories import PaymentDocumentRepository
from repositories.TicketRepository import TicketRepository
from repositories.InvoiceRepository import InvoiceRepository
from repositories.CartProductRepository import CartProductRepository
from services.FineService import FineService
from services.MembershipService import MembershipService
from services.EventsService import EventsService
from services.BungalowReservationService import BungalowReservationService

class PaymentService(object):

    __ticket_repository = TicketRepository()
    __invoice_repository = InvoiceRepository()
    __cart_product_repository = CartProductRepository()

    get_product_price = {
        '1': FineService.get,
        '2': MembershipService.get,
        '3': EventsService.get,
        '4': BungalowReservationService.findReservation,
        '5': EventsService.get
    }

    @classmethod
    def create(cls, insert_data):
        return cls.__paymentDocument_repository.create(insert_data)

    @classmethod
    def update(cls, id, update_data):
        return cls.__paymentDocument_repository.update(id, update_data)

    @classmethod
    def delete(cls, id):
        return cls.__paymentDocument_repository.delete(id)

    @classmethod
    def getPaymentDocuments(cls):
        return cls.__paymentDocument_repository.all()

    @classmethod
    def getPaymentDocument(cls, id):
        return cls.__paymentDocument_repository.find(id)

    @classmethod
    def payTicket(cls, products, member):

        subtotal = 0
        total_discount = 0
        igv_amount = 0

        for product in products:
            discount = product.discount
            subtotal += product.total
            total_discount += discount

        subtotal = subtotal - total_discount 
        igv_amount = subtotal*0.18
        total = subtotal + igv_amount

        insert_data = {
            'products': products,
            'subtotal': subtotal,
            'discounts': total_discount,
            'igv_amount': igv_amount,
            'total': total,
            'created_at': datetime.now()
        }

        if cls.__ticket_repository.create(insert_data):

            return products.update(status=1)

        return False

    @classmethod
    def payInvoice(cls, products, user_info):
        insert_data = {}
        new_invoice = cls.__invoice_repository.create(insert_data)

    @classmethod
    def getProductDiscount(cls, product, membership_type):
        pass        

    @classmethod
    def createEventProduct(cls, member, guests, event):

        if guests:
            insert_data = {
                'description': 'Ticket Invitado Evento:' + event.name,
                'quantity': guests,
                'product_type': 5,
                'product_id': event.pk,
                'member': member,
                'discount': 0,
                'total': guests*event.price_invited,
                'unit_price': event.price_invited,
            }

            cls.__cart_product_repository.create(insert_data)

        insert_data = {
            'description': 'Ticket Evento:' + event.name,
            'quantity': 1,
            'product_type': 3,
            'product_id': event.pk,
            'member': member,
            'discount': 0,
            'total': event.price_member,
            'unit_price': event.price_member,
        }

        return cls.__cart_product_repository.create(insert_data)

    @classmethod
    def createMembershipProduct(cls, membership, member):

        insert_data = {
            'description': 'Pago de Membresia:' + membership.membership_type.name,
            'quantity': 1,
            'product_type': 2,
            'product_id': membership.membership_type.pk,
            'member': member,
            'discount': 0,
            'total': membership.membership_type.price,
            'unit_price': membership.membership_type.price,
        }

        return cls.__cart_product_repository.create(insert_data)

    @classmethod
    def createFineProduct(cls, fine, member):

        insert_data = {
            'description': 'Pago de Multa:' + fine.fine_type.reason,
            'quantity': 1,
            'product_type': 1,
            'product_id': fine.pk,
            'member': member,
            'discount': 0,
            'total': fine.fine_type.price,
            'unit_price': fine.fine_type.price,
        }

        return cls.__cart_product_repository.create(insert_data)

    @classmethod
    def createBungalowReservationProduct(cls, bungalow_reservation, member):

        insert_data = {
            'description': 'Pago de Rerva Bungalow:' + bungalow_reservation.bungalow_number,
            'quantity': 1,
            'product_type': 4,
            'product_id': bungalow_reservation.pk,
            'member': member,
            'discount': 0,
            'total': bungalow_reservation.bungalow_price,
            'unit_price': bungalow_reservation.bungalow_price,
        }

        return cls.__cart_product_repository.create(insert_data)

    @classmethod
    def getCartProducts(cls, product_type, member):

        filters = {'member': member}
        if product_type:
            filters['product_type'] = product_type

        return cls.__cart_product_repository.filter(filters)

    @classmethod
    def payProducts(cls, payment_document_type, product_type, member, ruc, addres, social_reson):

        filters = {'status': 0}

        if product_type:
            filters['product_type'] = product_type

        products = member.cartproduct_set.filter(**filters)

        if payment_document_type == 'ticket':
            return cls.payTicket(products, member)

        return cls.payInvoice(products, member, ruc, addres, social_reson)