from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MemberService import MembersService
from services.MembershipService import MembershipService
from services.MembershipTypeService import MembershipTypeService
from services.AffiliateService import AffiliateService
from services.RelationshipService import RelationshipService
from django.views.decorators.http import require_http_methods
from services.IdentityDocumentTypeService import IdentityDocumentTypeService
from services.UbigeoService import UbigeoService
from services.SuspensionService import SuspensionService
from adapters.FormValidator import FormValidator
from adapters.DateManager import DateManager
from .forms import  AffiliateForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta


def isMemberSuspended(member):

    suspension_service = SuspensionService()

    filter_suspension = {}

    filter_suspension["membership"] = member.membership

    filter_suspension["status"] = 1

    suspensions = suspension_service.filter(filter_suspension)

    if len(suspensions) != 0:

        return True

    else:

        return False


@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['GET'])
def affiliate_index(request):

    user = request.user

    member_service = MembersService()

    member = member_service.getMemberByUser(user)

    id_member = member.id

    affiliate_service = AffiliateService()

    member = member_service.getMember(id_member)

    filter_affiliate = {}

    filter_affiliate["member"] = member

    filter_affiliate["state"] = 1

    affiliates = affiliate_service.filter(filter_affiliate)

    context = {
        'member' : member,
        'affiliates' : affiliates
    }

    return render(request, 'User/Affiliates/index_affiliates.html', context)


@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def create_index(request):

    id_member = request.POST['id']

    ubigeo_service = UbigeoService()

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    ubigeo = ubigeo_service.distinctDepartment()

    relationships_service = RelationshipService()

    relationships = relationships_service.getRelationships()

    context = {
        'id_member': id_member,
        'ubigeo': ubigeo,
        'doc_types': doc_types,
        'relationships': relationships
    }

    return render(request, 'User/Affiliates/new_affiliate.html', context)



@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def create_affiliate(request):

    id_member = request.POST['id_member']

    if "cancel" in request.POST:

        member_service = MembersService()

        affiliate_service = AffiliateService()

        member = member_service.getMember(id_member)

        filter_affiliate = {}

        filter_affiliate["member"] = member

        filter_affiliate["state"] = 1

        affiliates = affiliate_service.filter(filter_affiliate)

        context = {
            'member': member,
            'affiliates': affiliates,
        }

        return render(request, 'User/Affiliates/index_affiliates.html', context)

    form = AffiliateForm(request.POST)

    ubigeo_service = UbigeoService()

    identity_doc_type = request.POST['identity_document_type']

    relationshipID = request.POST['relationship']

    relationships_service = RelationshipService()

    if FormValidator.validateForm(form, request):

        identity_document_type_service = IdentityDocumentTypeService()

        doc_types = identity_document_type_service.getIdentityDocumentTypes()

        ubigeo = ubigeo_service.distinctDepartment()

        relationships = relationships_service.getRelationships()

        context = {
            'id_member': id_member,
            'ubigeo': ubigeo,
            'doc_types': doc_types,
            'relationships': relationships
        }

        return render(request, 'User/Affiliates/new_affiliate.html', context)

    else:

        create_data = {}

        create_data["identity_document_type_id"] = identity_doc_type

        create_data["name"] = form.cleaned_data['name']

        create_data["paternalLastName"] = form.cleaned_data['paternalLastName']

        create_data["maternalLastName"] = form.cleaned_data['maternalLastName']

        create_data["document_number"] = form.cleaned_data['num_doc']

        create_data["phone"] = form.cleaned_data['phone']

        create_data["address"] = form.cleaned_data['address']

        create_data["email"] = form.cleaned_data['email']

        create_data["member_id"] = id_member

        create_data["state"] = 1

        create_data['relationship'] = relationships_service.getRelationship(relationshipID)

        filter_ubigeo = {}

        filter_ubigeo["department"] = request.POST['department']

        filter_ubigeo["province"] = request.POST['province']

        filter_ubigeo["district"] = request.POST['district']

        ubi = ubigeo_service.filter(filter_ubigeo)

        create_data["ubigeo"] = ubi[0]

        create_data["photo"] = request.FILES['photo']

        create_data["gender"] = request.POST['gender']

        create_data["workPlace"] = form.cleaned_data['workPlace']

        create_data["workPlaceJob"] = form.cleaned_data['workPlaceJob']

        create_data["workPlacePhone"] = form.cleaned_data['workPlacePhone']

        create_data["nationality"] = form.cleaned_data['nationality']

        create_data["maritalStatus"] = form.cleaned_data['maritalStatus']

        create_data["cellphoneNumber"] = form.cleaned_data['cellphoneNumber']

        create_data["specialization"] = form.cleaned_data['specialization']

        create_data["birthDate"] = form.cleaned_data['birthDate']

        create_data["birthPlace"] = form.cleaned_data['birthPlace']

        filter_ubigeo["department"] = request.POST['birthDepartment']

        filter_ubigeo["province"] = request.POST['birthProvince']

        filter_ubigeo["district"] = request.POST['birthDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        create_data["birthUbigeo"] = ubi[0]

        affiliate_service = AffiliateService()

        affiliate_service.create(create_data)

        member_service = MembersService()

        member = member_service.getMember(id_member)

        filter_affiliate = {}

        filter_affiliate["member"] = member

        filter_affiliate["state"] = 1

        affiliates = affiliate_service.filter(filter_affiliate)

        context = {
            'member' : member,
            'affiliates' : affiliates,
            'affiliate_inserted':True
        }

        return render(request, 'User/Affiliates/index_affiliates.html', context)


@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def edit_affiliate_index(request):

    id_affiliate = request.POST['id']

    affiliate_service = AffiliateService()

    affiliate = affiliate_service.getAffiliate(id_affiliate)

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    relationships_service = RelationshipService()

    relationships = relationships_service.getRelationships()

    ubigeo_service = UbigeoService()

    departments = ubigeo_service.distinctDepartment()

    filter_ubigeo = {}

    filter_ubigeo["department"] = affiliate.ubigeo.department

    provinces = ubigeo_service.distinctProvince(filter_ubigeo)

    filter_ubigeo["province"] = affiliate.ubigeo.province

    districts = ubigeo_service.distinctDistrict(filter_ubigeo)

    filter_ubigeo = {}

    filter_ubigeo["department"] = affiliate.birthUbigeo.department

    birthprovinces = ubigeo_service.distinctProvince(filter_ubigeo)

    filter_ubigeo["province"] = affiliate.birthUbigeo.province

    birthdistricts = ubigeo_service.distinctDistrict(filter_ubigeo)

    affiliate.birthDate = datetime.strftime(affiliate.birthDate, '%m/%d/%Y')

    context = {
        'affiliate' : affiliate,
        'departments' : departments,
        'provinces' : provinces,
        'birthprovinces' : birthprovinces,
        'districts' : districts,
        'birthdistricts' : birthdistricts,
        'doc_types': doc_types,
        'relationships' : relationships
    }

    return render(request, 'User/Affiliates/edit_affiliate.html', context)


@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def edit_affiliate(request):

    id_edit = request.POST['id']

    if "cancel" in request.POST:
        member_service = MembersService()

        affiliate_service = AffiliateService()

        affiliate = affiliate_service.getAffiliate(id_edit)

        id_member = affiliate.member.id

        member = member_service.getMember(id_member)

        filter_affiliate = {}

        filter_affiliate["member"] = member

        filter_affiliate["state"] = 1

        affiliates = affiliate_service.filter(filter_affiliate)

        context = {
            'member': member,
            'affiliates': affiliates,
        }

        return render(request, 'User/Affiliates/index_affiliates.html', context)

    form = AffiliateForm(request.POST)

    ubigeo_service = UbigeoService()

    identity_doc_type = request.POST['identity_document_type']

    relationshipID = request.POST['relationship']

    relationships_service = RelationshipService()

    if FormValidator.validateForm(form, request):

        affiliate_service = AffiliateService()

        affiliate = affiliate_service.getAffiliate(id_edit)

        identity_document_type_service = IdentityDocumentTypeService()

        doc_types = identity_document_type_service.getIdentityDocumentTypes()

        ubigeo_service = UbigeoService()

        departments = ubigeo_service.distinctDepartment()

        filter_ubigeo = {}

        filter_ubigeo["department"] = affiliate.ubigeo.department

        provinces = ubigeo_service.distinctProvince(filter_ubigeo)

        filter_ubigeo["province"] = affiliate.ubigeo.province

        districts = ubigeo_service.distinctDistrict(filter_ubigeo)

        relationships = relationships_service.getRelationships()

        affiliate.birthDate = datetime.strftime(affiliate.birthDate, '%m/%d/%Y')

        filter_ubigeo = {}

        filter_ubigeo["department"] = affiliate.birthUbigeo.department

        birthprovinces = ubigeo_service.distinctProvince(filter_ubigeo)

        filter_ubigeo["province"] = affiliate.birthUbigeo.province

        birthdistricts = ubigeo_service.distinctDistrict(filter_ubigeo)

        context = {
            'affiliate': affiliate,
            'departments' : departments,
            'provinces' : provinces,
            'birthprovinces' : birthprovinces,
            'districts' : districts,
            'birthdistricts' : birthdistricts,
            'doc_types': doc_types,
            'relationships' : relationships
        }

        return render(request, 'User/Affiliates/edit_affiliate.html', context)

    else:

        edit_data = {}

        edit_data["identity_document_type_id"] = identity_doc_type

        edit_data['relationship'] = relationships_service.getRelationship(relationshipID)

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

        if 'photo' in request.FILES:
            edit_data["photo"] = request.FILES['photo']

        edit_data["gender"] = request.POST['gender']

        edit_data["workPlace"] = form.cleaned_data['workPlace']

        edit_data["workPlaceJob"] = form.cleaned_data['workPlaceJob']

        edit_data["workPlacePhone"] = form.cleaned_data['workPlacePhone']

        edit_data["nationality"] = form.cleaned_data['nationality']

        edit_data["maritalStatus"] = form.cleaned_data['maritalStatus']

        edit_data["cellphoneNumber"] = form.cleaned_data['cellphoneNumber']

        edit_data["specialization"] = form.cleaned_data['specialization']

        edit_data["birthDate"] = form.cleaned_data['birthDate']

        edit_data["birthPlace"] = form.cleaned_data['birthPlace']

        filter_ubigeo["department"] = request.POST['birthDepartment']

        filter_ubigeo["province"] = request.POST['birthProvince']

        filter_ubigeo["district"] = request.POST['birthDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        edit_data["birthUbigeo"] = ubi[0]

        affiliate_service = AffiliateService()

        affiliate_service.update(id_edit, edit_data)

        affiliate = affiliate_service.getAffiliate(id_edit)

        id_member = affiliate.member.id

        filter_affiliate = {}

        filter_affiliate["member"] = affiliate.member

        filter_affiliate["state"] = 1

        affiliates = affiliate_service.filter(filter_affiliate)

        context = {
            'member' : affiliate.member,
            'affiliates' : affiliates,
            'affiliate_edited':True
        }

        return render(request, 'User/Affiliates/index_affiliates.html', context)


@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def delete_affiliate(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["state"] = 0

    affiliate_service = AffiliateService()

    affiliate_service.update(id_edit, edit_data)

    affiliate = affiliate_service.getAffiliate(id_edit)

    filter_affiliate = {}

    filter_affiliate["member"] = affiliate.member

    filter_affiliate["state"] = 1

    affiliates = affiliate_service.filter(filter_affiliate)

    context = {
        'member' : affiliate.member,
        'affiliates' : affiliates,
        'affiliate_deleted':True
    }

    return render(request, 'User/Affiliates/index_affiliates.html', context)



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def admin_affiliate_index(request):

    id_member = request.POST['id']

    member_service = MembersService()

    affiliate_service = AffiliateService()

    member = member_service.getMember(id_member)

    filter_affiliate = {}

    filter_affiliate["member"] = member

    filter_affiliate["state"] = 1

    affiliates = affiliate_service.filter(filter_affiliate)

    isSuspended = isMemberSuspended(member)

    context = {
        'member' : member,
        'affiliates' : affiliates,
        'isSuspended' : isSuspended
    }

    return render(request, 'Admin/Affiliates/index_affiliates.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def admin_create_index(request):

    id_member = request.POST['id']

    ubigeo_service = UbigeoService()

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    relationships_service = RelationshipService()

    relationships = relationships_service.getRelationships()

    ubigeo = ubigeo_service.distinctDepartment()

    context = {
        'id_member': id_member,
        'ubigeo': ubigeo,
        'doc_types': doc_types,
        'relationships' : relationships
    }

    return render(request, 'Admin/Affiliates/new_affiliate.html', context)



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def admin_create_affiliate(request):

    id_member = request.POST['id_member']

    if "cancel" in request.POST:

        member_service = MembersService()

        affiliate_service = AffiliateService()

        member = member_service.getMember(id_member)

        filter_affiliate = {}

        filter_affiliate["member"] = member

        filter_affiliate["state"] = 1

        affiliates = affiliate_service.filter(filter_affiliate)

        isSuspended = isMemberSuspended(member)

        context = {
            'member' : member,
            'affiliates' : affiliates,
            'isSuspended' : isSuspended
        }

        return render(request, 'Admin/Affiliates/index_affiliates.html', context)

    form = AffiliateForm(request.POST)

    ubigeo_service = UbigeoService()

    identity_doc_type = request.POST['identity_document_type']

    relationshipID = request.POST['relationship']

    relationships_service = RelationshipService()

    if FormValidator.validateForm(form, request):

        identity_document_type_service = IdentityDocumentTypeService()

        doc_types = identity_document_type_service.getIdentityDocumentTypes()

        relationships = relationships_service.getRelationships()

        ubigeo = ubigeo_service.distinctDepartment()

        context = {
            'id_member': id_member,
            'ubigeo': ubigeo,
            'doc_types': doc_types,
            'relationships' : relationships
        }

        return render(request, 'Admin/Affiliates/new_affiliate.html', context)

    else:

        create_data = {}

        create_data["identity_document_type_id"] = identity_doc_type

        relationship=relationships_service.getRelationship(relationshipID)

        create_data["relationship"] = relationship

        create_data["name"] = form.cleaned_data['name']

        create_data["paternalLastName"] = form.cleaned_data['paternalLastName']

        create_data["maternalLastName"] = form.cleaned_data['maternalLastName']

        create_data["document_number"] = form.cleaned_data['num_doc']

        create_data["phone"] = form.cleaned_data['phone']

        create_data["address"] = form.cleaned_data['address']

        create_data["email"] = form.cleaned_data['email']

        create_data["member_id"] = id_member

        create_data["state"] = 1

        filter_ubigeo = {}

        filter_ubigeo["department"] = request.POST['department']

        filter_ubigeo["province"] = request.POST['province']

        filter_ubigeo["district"] = request.POST['district']

        ubi = ubigeo_service.filter(filter_ubigeo)

        create_data["ubigeo"] = ubi[0]

        create_data["photo"] = request.FILES['photo']

        create_data["gender"] = request.POST['gender']

        create_data["workPlace"] = form.cleaned_data['workPlace']

        create_data["workPlaceJob"] = form.cleaned_data['workPlaceJob']

        create_data["workPlacePhone"] = form.cleaned_data['workPlacePhone']

        create_data["nationality"] = form.cleaned_data['nationality']

        create_data["maritalStatus"] = form.cleaned_data['maritalStatus']

        create_data["cellphoneNumber"] = form.cleaned_data['cellphoneNumber']

        create_data["specialization"] = form.cleaned_data['specialization']

        create_data["birthDate"] = form.cleaned_data['birthDate']

        create_data["birthPlace"] = form.cleaned_data['birthPlace']

        filter_ubigeo["department"] = request.POST['birthDepartment']

        filter_ubigeo["province"] = request.POST['birthProvince']

        filter_ubigeo["district"] = request.POST['birthDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        create_data["birthUbigeo"] = ubi[0]

        affiliate_service = AffiliateService()

        affiliate_service.create(create_data)

        member_service = MembersService()

        member = member_service.getMember(id_member)

        filter_affiliate = {}

        filter_affiliate["member"] = member

        filter_affiliate["state"] = 1

        affiliates = affiliate_service.filter(filter_affiliate)

        isSuspended = isMemberSuspended(member)

        context = {
            'member' : member,
            'affiliates' : affiliates,
            'isSuspended' : isSuspended,
            'affiliate_inserted':True
        }

        return render(request, 'Admin/Affiliates/index_affiliates.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def admin_edit_affiliate_index(request):

    id_affiliate = request.POST['id']

    affiliate_service = AffiliateService()

    affiliate = affiliate_service.getAffiliate(id_affiliate)

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    relationships_service = RelationshipService()

    relationships = relationships_service.getRelationships()

    ubigeo_service = UbigeoService()

    departments = ubigeo_service.distinctDepartment()

    filter_ubigeo = {}

    filter_ubigeo["department"] = affiliate.ubigeo.department

    provinces = ubigeo_service.distinctProvince(filter_ubigeo)

    filter_ubigeo["province"] = affiliate.ubigeo.province

    districts = ubigeo_service.distinctDistrict(filter_ubigeo)

    filter_ubigeo = {}

    filter_ubigeo["department"] = affiliate.birthUbigeo.department

    birthprovinces = ubigeo_service.distinctProvince(filter_ubigeo)

    filter_ubigeo["province"] = affiliate.birthUbigeo.province

    birthdistricts = ubigeo_service.distinctDistrict(filter_ubigeo)



    affiliate.birthDate = datetime.strftime(affiliate.birthDate, '%m/%d/%Y')

    context = {
        'affiliate' : affiliate,
        'departments' : departments,
        'provinces' : provinces,
        'birthprovinces' : birthprovinces,
        'districts' : districts,
        'birthdistricts' : birthdistricts,
        'doc_types': doc_types,
        'relationships' : relationships
    }

    return render(request, 'Admin/Affiliates/edit_affiliate.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def admin_edit_affiliate(request):

    id_edit = request.POST['id']

    if "cancel" in request.POST:
        member_service = MembersService()

        affiliate_service = AffiliateService()

        affiliate = affiliate_service.getAffiliate(id_edit)

        id_member = affiliate.member.id

        member = member_service.getMember(id_member)

        filter_affiliate = {}

        filter_affiliate["member"] = member

        filter_affiliate["state"] = 1

        affiliates = affiliate_service.filter(filter_affiliate)

        isSuspended = isMemberSuspended(member)

        context = {
            'member' : member,
            'affiliates' : affiliates,
            'isSuspended' : isSuspended
        }

        return render(request, 'Admin/Affiliates/index_affiliates.html', context)

    form = AffiliateForm(request.POST)

    ubigeo_service = UbigeoService()

    identity_doc_type = request.POST['identity_document_type']

    relationshipID = request.POST['relationship']

    relationships_service = RelationshipService()

    if FormValidator.validateForm(form, request):

        affiliate_service = AffiliateService()

        affiliate = affiliate_service.getAffiliate(id_edit)

        identity_document_type_service = IdentityDocumentTypeService()

        doc_types = identity_document_type_service.getIdentityDocumentTypes()

        ubigeo_service = UbigeoService()

        departments = ubigeo_service.distinctDepartment()

        filter_ubigeo = {}

        filter_ubigeo["department"] = affiliate.ubigeo.department

        provinces = ubigeo_service.distinctProvince(filter_ubigeo)

        filter_ubigeo["province"] = affiliate.ubigeo.province

        districts = ubigeo_service.distinctDistrict(filter_ubigeo)

        filter_ubigeo = {}

        filter_ubigeo["department"] = affiliate.birthUbigeo.department

        birthprovinces = ubigeo_service.distinctProvince(filter_ubigeo)

        filter_ubigeo["province"] = affiliate.birthUbigeo.province

        birthdistricts = ubigeo_service.distinctDistrict(filter_ubigeo)

        relationships = relationships_service.getRelationships()

        affiliate.birthDate = datetime.strftime(affiliate.birthDate, '%m/%d/%Y')

        context = {
            'affiliate' : affiliate,
            'departments' : departments,
            'provinces' : provinces,
            'birthprovinces' : birthprovinces,
            'districts' : districts,
            'birthdistricts' : birthdistricts,
            'doc_types': doc_types,
            'relationships' : relationships
        }

        return render(request, 'Admin/Affiliates/edit_affiliate.html', context)

    else:

        edit_data = {}

        edit_data["identity_document_type_id"] = identity_doc_type

        edit_data['relationship'] = relationships_service.getRelationship(relationshipID)

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

        if 'photo' in request.FILES:
            edit_data["photo"] = request.FILES['photo']

        edit_data["gender"] = request.POST['gender']

        edit_data["workPlace"] = form.cleaned_data['workPlace']

        edit_data["workPlaceJob"] = form.cleaned_data['workPlaceJob']

        edit_data["workPlacePhone"] = form.cleaned_data['workPlacePhone']

        edit_data["nationality"] = form.cleaned_data['nationality']

        edit_data["maritalStatus"] = form.cleaned_data['maritalStatus']

        edit_data["cellphoneNumber"] = form.cleaned_data['cellphoneNumber']

        edit_data["specialization"] = form.cleaned_data['specialization']

        edit_data["birthDate"] = form.cleaned_data['birthDate']

        edit_data["birthPlace"] = form.cleaned_data['birthPlace']

        filter_ubigeo["department"] = request.POST['birthDepartment']

        filter_ubigeo["province"] = request.POST['birthProvince']

        filter_ubigeo["district"] = request.POST['birthDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        edit_data["birthUbigeo"] = ubi[0]

        affiliate_service = AffiliateService()

        member_service = MembersService()

        affiliate_service.update(id_edit, edit_data)

        affiliate = affiliate_service.getAffiliate(id_edit)

        member = affiliate.member

        filter_affiliate = {}

        filter_affiliate["member"] = member

        filter_affiliate["state"] = 1

        affiliates = affiliate_service.filter(filter_affiliate)

        isSuspended = isMemberSuspended(member)

        context = {
            'member' : member,
            'affiliates' : affiliates,
            'isSuspended' : isSuspended,
            'affiliate_edited':True
        }

        return render(request, 'Admin/Affiliates/index_affiliates.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def admin_delete_affiliate(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["state"] = 0

    affiliate_service = AffiliateService()

    affiliate_service.update(id_edit, edit_data)

    affiliate = affiliate_service.getAffiliate(id_edit)

    member = affiliate.member

    filter_affiliate = {}

    filter_affiliate["member"] = member

    filter_affiliate["state"] = 1

    affiliates = affiliate_service.filter(filter_affiliate)

    isSuspended = isMemberSuspended(affiliate.member)

    context = {
        'member' : member,
        'affiliates' : affiliates,
        'isSuspended' : isSuspended,
        'affiliate_deleted':True
    }

    return render(request, 'Admin/Affiliates/index_affiliates.html', context)



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def admin_move_affiliate(request):

    id_edit = request.POST['id']

    edit_data = {}

    edit_data["state"] = 0

    edit_data2 = {}

    edit_data2["status"] = 0

    affiliate_service = AffiliateService()

    member_service = MembersService()

    membership_service = MembershipService()

    membership_type_service = MembershipTypeService()
    
    affiliate = affiliate_service.getAffiliate(id_edit)

    member = affiliate.member

    membership = member.membership

    #Create new user

    password = get_random_string(length=10)

    email = EmailMessage('Traslado de membresia' ,
                             'Hola ' + member.name + ',\n\nHemos procesado el traslado de tu membresia a '+
                             affiliate.name + ' ' + affiliate.paternalLastName + '.', 
                             to=[member.email])

    email.send()


    email = EmailMessage('Traslado de membresia' ,
                             'Hola ' + affiliate.name + ',\n\nHemos procesado el traslado de membresia.'+
                             '\n\n\nPara poder acceder al sistema utiliza los siguientes datos: '+
                             '\nUsuario:    '+ str(affiliate.document_number) +
                             '\nContraseña: '+ str(password), 
                             to=[affiliate.email])

    email.send()

    user = User.objects.create_user(username=str(affiliate.document_number), email=affiliate.email,   password=password, first_name=affiliate.name, last_name=affiliate.paternalLastName)

    group = Group.objects.get(name='usuarios')

    group.user_set.add(user)

    #Create new membership

    insert_data_membership = {}

    filter_membership_type = {}

    filter_membership_type["name"] = 'Vitalicio'

    membership_type = membership_type_service.filter(filter_membership_type)[0]

    if(membership_type.id == membership.membership_type.id):
        #Miembro vitalicio

        filter_membership_type["name"] = 'Miembro'
        
        insert_data_membership["membership_type"] = membership_type_service.filter(filter_membership_type)[0]

        insert_data_membership["initialDate"] = datetime.now()

        final_date = datetime.now()

        months = 10

        final_date = DateManager.add_months(final_date, months)

        insert_data_membership["finalDate"] = final_date
            

    else:   

        insert_data_membership["membership_type"] = membership.membership_type

        insert_data_membership["initialDate"] = membership.initialDate

        insert_data_membership["finalDate"] = membership.finalDate

    insert_data_membership["status"] = 1

    newMembership = membership_service.create(insert_data_membership)

    #Create new member

    insert_data = {}

    insert_data["user_id"] = user.id

    insert_data["membership"] = newMembership

    insert_data['identity_document_type_id'] = affiliate.identity_document_type.id

    insert_data["name"] = affiliate.name

    insert_data["paternalLastName"] = affiliate.paternalLastName

    insert_data["maternalLastName"] = affiliate.maternalLastName

    insert_data["document_number"] = affiliate.document_number

    insert_data["phone"] = affiliate.phone

    insert_data["address"] = affiliate.address

    insert_data["email"] = affiliate.email

    insert_data["photo"] = affiliate.photo

    insert_data["gender"] = affiliate.gender

    insert_data["workPlace"] = affiliate.workPlace

    insert_data["workPlaceJob"] = affiliate.workPlaceJob

    insert_data["workPlacePhone"] = affiliate.workPlacePhone

    insert_data["nationality"] = affiliate.nationality

    insert_data["maritalStatus"] = affiliate.maritalStatus

    insert_data["cellphoneNumber"] = affiliate.cellphoneNumber

    insert_data["specialization"] = affiliate.specialization

    insert_data["birthDate"] = affiliate.birthDate

    insert_data["birthPlace"] = affiliate.birthPlace

    ubigeo_service = UbigeoService()

    ubi = ubigeo_service.getUbigeoById(affiliate.birthUbigeo.id)

    insert_data["birthUbigeo"] = ubi

    insert_data["state"] = 1

    ubigeo_service = UbigeoService()

    ubi = ubigeo_service.getUbigeoById(affiliate.ubigeo.id)

    insert_data["ubigeo"] = ubi

    member_service.create(insert_data)

    #Delete previous member, membership and its affiliates

    filter_data = {}

    filter_data["state"] = 1

    filter_data["member"] = member

    affiliates = affiliate_service.filter(filter_data)

    for aff in affiliates:
    
        affiliate_service.update(aff.id, edit_data)

    membership_service.update(membership.id,edit_data2)

    member_service.update(member.id,edit_data)    
    
    return HttpResponseRedirect(reverse('members:index'))



@login_required
@require_http_methods(['POST'])
def verify_affiliate(request):

    member_application_service = Membership_ApplicationService()

    member_service = MembersService()

    affiliate_service = AffiliateService()

    filter_data = {}

    filter_data["document_number"] = request.POST['num_doc']

    filter_data["status"] = 1

    filter_data2 = {}

    filter_data2["document_number"] = request.POST['num_doc']

    filter_data2["state"] = 1
    
    if( member_application_service.filter(filter_data)):

        return  HttpResponse("false")

    affiliates = affiliate_service.filter(filter_data2)

    if(affiliates):

        affiliate = affiliates[0]

        if(str(affiliate.document_number) == request.POST['num_doc']):
            
            return  HttpResponse("true")

        return  HttpResponse("false")

    if(member_service.filter(filter_data2)):

        return  HttpResponse("false")

    return  HttpResponse("true")

