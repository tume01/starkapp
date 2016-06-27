from datetime import datetime,timedelta
from repositories import PaymentDocumentRepository
from repositories.TicketRepository import TicketRepository
from repositories.InvoiceRepository import InvoiceRepository
from repositories.CartProductRepository import CartProductRepository
from services.FineService import FineService
from services.MembershipService import MembershipService
from services.EventsService import EventsService
from services.BungalowReservationService import BungalowReservationService
from itertools import chain
from adapters.DateManager import DateManager
from services.FineService import FineService
from django.db.models import Sum

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

    finish_products = {
        '1': FineService.get,
        '2': MembershipService.get,
        #'3': registerEvent,
        '4': BungalowReservationService.findReservation,
        '5': EventsService.get
    }

    @classmethod
    def registerEvent(cls, member, events):
        event_service = EventsService()
        guests = cls.getCartProducts(5, member)
        for event in events:
            print('eventos')
            guest_amount = 0
            for guest in guests:
                if guest.product_id == event.product_id:
                    guest_amount += guest.quantity
            guests.update(status=1)  
            event_service.registerMember(event.product_id, member, guest_amount)
        return True

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
    def registerMembership(cls, member, products):
        membership_service = MembershipService()

        for product in products:
            membership = membership_service.getMembership(product.product_id) 
            extra_time = DateManager.add_months(membership.finalDate, 12)
            membership.finalDate=extra_time
            membership.save()
        return True
    
    @classmethod 
    def registerFine(cls, member, products):
        fine_service = FineService()
        print(products)
        for product in products:
            fine = fine_service.getFine(product.product_id)
            fine.status = 'Pagada'
            fine.save()

        return True

    @classmethod
    def payTicket(cls, products, member):

        subtotal = 0
        total_discount = 0
        igv_amount = 0
        total_producs = products

        if products.first().product_type == 3:
            total_producs = list(chain(products, cls.getCartProducts(5, member)))

        for product in total_producs:
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
            product_type = products.first().product_type

            if product_type == 3:
                cls.registerEvent(member, products)
            elif product_type == 2:
                cls.registerMembership(member, products)
            elif product_type == 1:
                cls.registerFine(member, products)

            return products.update(status=1)

        return False

    @classmethod
    def payInvoice(cls, products, member, ruc, addres, social_reson):

        subtotal = 0
        total_discount = 0
        igv_amount = 0
        total_producs = products
        if products.first().product_type == 3:
            total_producs = list(chain(products, cls.getCartProducts(5, member)))
        for product in total_producs:
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
            'created_at': datetime.now(),
            'name': addres,
            'ruc': ruc,
            'address': addres
        }

        if cls.__invoice_repository.create(insert_data):
            if products.first().product_type == 3:
                cls.registerEvent(member, products)
            elif product_type == 2:
                cls.registerMembership(member, products)
            elif product_type == 1:
                cls.registerFine(member, products)
  

            return products.update(status=1)
        return False


    @classmethod
    def getEventDiscount(cls, event, membership_type):
        
        discounts =  event.event_type.eventpromotion_set.filter(membership_type=membership_type)

        if discounts:
            return discounts.aggregate(Sum('percentage'))['percentage__sum'] / 100

        return 0

    @classmethod
    def getMembershipDiscount(cls, membership_type):
        
        discounts =  membership_type.membershippromotion_set.all()

        if discounts:
            return discounts.aggregate(Sum('percentage'))['percentage__sum'] / 100
            
        return 0

    @classmethod
    def createEventProduct(cls, member, guests, event):

        assistants = event.eventregistration_set.filter(deleted_at=None).count()
        
        if member.eventregistration_set.filter(event_id=event.pk).count():
            return None

        if not event.assistance > assistants:
            return None

        
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
            'discount': cls.getEventDiscount(event, member.membership.membership_type)*event.price_member,
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
            'product_id': membership.pk,
            'member': member,
            'discount': cls.getMembershipDiscount(membership.membership_type)*membership.membership_type.price,
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
            'description': 'Pago de Rerva Bungalow:' + str(bungalow_reservation.bungalow_number),
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

        filters = {'member': member, 'status': 0}

        if product_type:
            filters['product_type'] = product_type

        return cls.__cart_product_repository.filter(filters)

    @classmethod
    def payProducts(cls, payment_document_type, product_type, member, ruc, addres, social_reson):

        filters = {'status': 0}
        if product_type:
            filters['product_type'] = product_type
            if product_type == '3':
                guests = cls.getCartProducts(5, member)

        products = member.cartproduct_set.filter(**filters)

        if payment_document_type == 'ticket':
            return cls.payTicket(products, member)
 
        return cls.payInvoice(products, member, ruc, addres, social_reson)