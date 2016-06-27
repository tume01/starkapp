from django.db.models import Sum
from django.shortcuts import render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from services.PaymentService import PaymentService
from services.MemberService import MembersService
import json
from services.EventsService import EventsService
from django.core.urlresolvers import reverse
from itertools import chain
# Create your views here.

def index(request):
    
    product_type = request.GET.get('product_type', None)

    member_service = MembersService()
    member = member_service.getMemberByUser(request.user)

    products = PaymentService.getCartProducts(product_type, member)
    product_list = products
    guests_subtotal = 0
    guests_discounts = 0

    if product_type == '3':
        guests = PaymentService.getCartProducts(5, member)
        guests_subtotal = guests.aggregate(Sum('total'))['total__sum']
        guests_discounts = guests.aggregate(Sum('discount'))['discount__sum']
        product_list = list(chain(products, guests))

    subtotal = 0
    discount  = 0
    igv_total = 0
    total = 0
    
    if products:
        subtotal = products.aggregate(Sum('total'))['total__sum'] + guests_subtotal
        discount = products.aggregate(Sum('discount'))['discount__sum'] + guests_discounts
        igv_total = round(0.18*(subtotal - discount), 2)
        total = subtotal - discount + igv_total
    
    context = {
        'products': product_list,
        'product_type': product_type,
        'subtotal': subtotal,
        'igv_total': igv_total,
        'discount': discount,
        'total': total
    }

    return render(request, 'User/Checkout/index.html', context)

def pay(request):

    member_service = MembersService()
    member = member_service.getMemberByUser(request.user)
    event_service = EventsService()

    product_type = request.POST.get('product_type', None)
    payment_document_type = request.POST.get('payment')
    ruc = request.POST.get('ruc', '')
    address = request.POST.get('address', '')
    social_reason = request.POST.get('social_reason', '')

    if PaymentService.payProducts(payment_document_type, product_type, member, ruc, address, social_reason):
        return HttpResponseRedirect(reverse('login:iniUser'))
        
    