from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MemberService import MembersService
from django.views.decorators.http import require_http_methods
from services.IdentityDocumentTypeService import IdentityDocumentTypeService
from services.UbigeoService import UbigeoService
from services.GuestService import GuestService
from services.SuspensionService import SuspensionService
from services.AffiliateService import AffiliateService
from Adapters.FormValidator import FormValidator
from .forms import  MemberForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core import serializers
import json


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['GET'])
def member_index(request):

    member_service = MembersService()

    identity_service = IdentityDocumentTypeService()

    members = member_service.getMembers()

    doc_types = identity_service.getIdentityDocumentTypes()

    context = {
        'members' : members,
        'doc_types' : doc_types
    }

    return render(request, 'Admin/Members/index_members.html', context) 


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_member_index(request):

    id_member = request.POST['id']

    member_service = MembersService()

    member = member_service.getMember(id_member)

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    ubigeo_service = UbigeoService()

    departments = ubigeo_service.distinctDepartment()

    filter_ubigeo = {}

    filter_ubigeo["department"] = member.ubigeo.department

    provinces = ubigeo_service.distinctProvince(filter_ubigeo)

    filter_ubigeo = {}

    filter_ubigeo["province"] = member.ubigeo.province

    districts = ubigeo_service.distinctDistrict(filter_ubigeo)

    context = {
        'member' : member,
        'departments' : departments,
        'provinces' : provinces,
        'districts' : districts,
        'doc_types': doc_types,
    }

    return render(request, 'Admin/Members/edit_member.html', context)



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def delete_member(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["state"] = 0

    member_service = MembersService()

    member_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('members:index'))




@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_member(request):

    form = MemberForm(request.POST)

    id_edit = request.POST['id']

    ubigeo_service = UbigeoService()

    identity_doc_type = request.POST['identity_document_type']

    if FormValidator.validateForm(form, request):

        member_service = MembersService()

        member = member_service.getMember(id_edit)

        identity_document_type_service = IdentityDocumentTypeService()

        doc_types = identity_document_type_service.getIdentityDocumentTypes()

        ubigeo = ubigeo_service.getAllUbigeo()

        context = {
            'member': member,
            'ubigeo': ubigeo,
            'doc_types': doc_types
        }

        return render(request, 'Admin/Members/edit_member.html', context)

    else:

        edit_data = {}

        edit_data["identity_document_type_id"] = identity_doc_type

        edit_data["name"] = form.cleaned_data['name']

        edit_data["paternalLastName"] = form.cleaned_data['paternalLastName']

        edit_data["maternalLastName"] = form.cleaned_data['maternalLastName']

        edit_data["document_number"] = form.cleaned_data['num_doc']

        edit_data["phone"] = form.cleaned_data['phone']

        edit_data["address"] = form.cleaned_data['address']

        edit_data["email"] = form.cleaned_data['email']

        filter_ubigeo = {}

        filter_ubigeo["department"] = request.POST['department']

        filter_ubigeo["province"] = request.POST['province']

        filter_ubigeo["district"] = request.POST['district']

        ubi = ubigeo_service.filter(filter_ubigeo)

        edit_data["ubigeo"] = ubi[0]

        member_service = MembersService()

        member_service.update(id_edit, edit_data)

        return HttpResponseRedirect(reverse('members:index'))


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def member_filter(request):

    member_service = MembersService()

    identity_service = IdentityDocumentTypeService()

    doc_types = identity_service.getIdentityDocumentTypes()

    filter_member = {}

    name = request.POST['name']

    paternalLastName = request.POST['paternalLastName']

    maternalLastName = request.POST['maternalLastName']

    document = request.POST['num_doc']

    suspended = request.POST['suspended']

    identity_document_type = request.POST['identity_document_type']

    if paternalLastName != '':
        filter_member['paternalLastName'] = paternalLastName

    if maternalLastName != '':
        filter_member['maternalLastName'] = maternalLastName

    if document != '':
        filter_member['document'] = document

    if name != '':
        filter_member['name'] = name

    if identity_document_type != 'Todos':
        filter_member['identity_document_type'] = identity_document_type

    members = member_service.filter(filter_member)

    if suspended == 1:
        members = filter(is_member_suspended, members)

        context = {
            'members': members,
            'doc_types': doc_types
        }

        return render(request, 'Admin/Members/index_members.html', context)

    if suspended == 0:
        members = filter(not is_member_suspended, members)

        context = {
            'members': members,
            'doc_types': doc_types
        }

        return render(request, 'Admin/Members/index_members.html', context)

    context = {
        'members': members,
        'doc_types': doc_types
    }

    return render(request, 'Admin/Members/index_members.html', context)


def is_member_suspended(member):

    suspension_service = SuspensionService()

    filter_data = {}

    filter_data['membership_id'] = member.id

    member_suspensions = suspension_service.filter(filter_data)

    return any(s.status == 1 for s in member_suspensions)


@login_required
@require_http_methods(['POST'])
def get_member(request):

    member_service = MembersService()

    doc=request.POST['document_number']

    if(not doc.isdigit()):

        return  HttpResponse("")

    filter_member = {}

    filter_member["document_number"] = doc

    member = member_service.filter(filter_member)

    member = serializers.serialize('json', member)

    return  HttpResponse(member, content_type = "application/json")


@login_required
@require_http_methods(['POST'])
def get_entry(request):

    member_service = MembersService()

    filter_member = {}

    filter_member["document_number"] = request.POST['document_number']

    member = member_service.filter(filter_member)

    if(member):      

        member = serializers.serialize("json", (member[0],))

        resp_obj = json.loads(member)

        resp_obj[0]['fields']['tipo'] = 1

        member = json.dumps(resp_obj)

        return  HttpResponse(member, content_type = "application/json")

    affiliate_service = AffiliateService()

    filter_affiliate = {}

    filter_affiliate["document_number"] = request.POST['document_number']

    affiliate = affiliate_service.filter(filter_affiliate)

    if(affiliate):   

        affiliate = serializers.serialize("json", (affiliate[0],))

        resp_obj = json.loads(affiliate)

        resp_obj[0]['fields']['tipo'] = 2

        affiliate = json.dumps(resp_obj)

        return  HttpResponse(affiliate, content_type = "application/json")

    guest_service = GuestService()

    filter_guest = {}

    filter_guest["dni"] = request.POST['document_number']

    guest = guest_service.filter(filter_guest)

    if(guest):

        guest = serializers.serialize("json", (guest[0],))

        resp_obj = json.loads(guest)

        resp_obj[0]['fields']['tipo'] = 3

        guest = json.dumps(resp_obj)

        return  HttpResponse(guest, content_type = "application/json")

    guest = serializers.serialize('json', guest)

    return  HttpResponse(guest, content_type = "application/json")
