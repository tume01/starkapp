from django.shortcuts import render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from services.PaymentService import PaymentService
from services.MemberService import MembersService
# Create your views here.

def index(request):
    
    product_type = request.GET.get('product_type', None)

    member_service = MembersService()
    member = member_service.getMemberByUser(request.user)

    products = PaymentService.getCartProducts(product_type, member)
    
    context = {
        'products': products,
        'product_type': product_type
    }

    return render(request, 'User/Checkout/index.html', context)

def pay(request):

    member_service = MembersService()
    member = member_service.getMemberByUser(request.user)
    
    product_type = request.POST.get('product_type', None)

    PaymentService.payProducts(payment_document_type, product_type, member)

    return HttpResponse('holi')