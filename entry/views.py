from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from services.EntryService import EntryService
from services.MemberService import MembersService
from services.GuestService import GuestService
from services.AffiliateService import AffiliateService
from services.IdentityDocumentTypeService import IdentityDocumentTypeService
from services.PaymentDocumentTypeService import PaymentDocumentTypeService
from datetime import datetime

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def index(request):


    entry_service = EntryService()

    entries = entry_service.getEntries()

    #payment_document_types_service = PaymentDocumentTypeService()

    identity_document_type_service = IdentityDocumentTypeService()

    #payment_document_types = payment_document_types_service.getDocumentTypes()

    identity_document_types = identity_document_type_service.getIdentityDocumentTypes()

    context = {
        'entries' : entries,
        #'payment_document_types': payment_document_types,
        'identity_document_types': identity_document_types,
    }

    return render(request, 'Admin/Guests/index_entries.html', context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def index_filter(request):

    entry_service = EntryService()

    #payment_document_types_service = PaymentDocumentTypeService()

    identity_document_type_service = IdentityDocumentTypeService()

    #payment_document_types = payment_document_types_service.getDocumentTypes()

    identity_document_types = identity_document_type_service.getIdentityDocumentTypes()

    filter_entries = {}

    iniDate = request.POST['initialDate']

    endDate = request.POST['finalDate']

    numIdentityDoc = request.POST['num_doc']

    identityDocId = request.POST['identity_doc']

    #paymentDocId = request.POST['payment_doc_id']

    if iniDate != '':
        filter_entries["initialDate__gte"] = datetime.strptime(iniDate, '%m/%d/%Y')

    if endDate != '':
        filter_entries["finalDate__lte"] = datetime.strptime(endDate, '%m/%d/%Y')

    entries = entry_service.filter(filter_entries)

    if identityDocId != 'Todos':
        entries = filter(lambda entry: entry.member.identity_document_type.id == int(identityDocId), entries)

    if numIdentityDoc != '':
        entries = filter(lambda entry: entry.member.document_number == int(numIdentityDoc),entries)

    #if paymentDocId != 'Todos':
        #entries = filter(lambda entry: entry.payment_document.id == paymentDocId,entries)

    context = {
        'entries': entries,
        #'payment_document_types' : payment_document_types,
        'identity_document_types' : identity_document_types,
    }

    return render(request, 'Admin/Guests/index_entries.html', context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Guests/new_guests_members.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def insert(request):

    insert_data = {}

    type = request.POST['type']

    #busco al responsable

    filter_data = {}

    member_service = MembersService()

    affiliate_service = AffiliateService()

    if(type == '2'):

        filter_data["document_number"] = request.POST['document_number_mem']

        affiliate = affiliate_service.filter(filter_data)

        insert_data["member"] = affiliate[0].member

    else:

        filter_data["document_number"] = request.POST['document_number_mem']

        member = member_service.filter(filter_data)

        insert_data["member"] = member[0]

    #1 para miembro, 2 para afiliado, 3 para invitado, 0 para nuevo invitado
    if(type == '2'):

        filter_data = {}

        filter_data["document_number"] = request.POST['document_number']

        filter_data["state"] = 1

        affiliate = affiliate_service.filter(filter_data)

        insert_data["affiliate"] = affiliate[0]

    elif(type == '3'):

        guest_service = GuestService()

        filter_data = {}

        filter_data["document_number"] = request.POST['document_number']

        guest = guest_service.filter(filter_data)

        insert_data["guest"] = guest[0]

    elif(type == '0'):

        insert_guest = {}

        insert_guest["name"] = request.POST['name']

        insert_guest["paternalLastName"] = request.POST['paternalLastName']

        insert_guest["document_number"] = request.POST['document_number']

        insert_guest["status"] = 1

        guest_service = GuestService()

        guest = guest_service.create(insert_guest)

        insert_data["guest"] = guest

    insert_data["initialDate"] = datetime.strptime(request.POST['initialDate'], '%m/%d/%Y')

    insert_data["finalDate"] = datetime.strptime(request.POST['finalDate'], '%m/%d/%Y')

    entry_service = EntryService()

    entry_service.create(insert_data)

    return HttpResponseRedirect(reverse('entry:index'))


@login_required
@require_http_methods(['POST'])
def verify_member(request):

    member_service = MembersService()

    filter_member = {}

    filter_member["document_number"] = request.POST['document_number']

    member = member_service.filter(filter_member)

    if(member):      

        return  HttpResponse("true")

    affiliate_service = AffiliateService()

    filter_affiliate = {}

    filter_affiliate["document_number"] = request.POST['document_number']

    affiliate = affiliate_service.filter(filter_affiliate)

    if(affiliate):   

        return  HttpResponse("true")

    return  HttpResponse("false")