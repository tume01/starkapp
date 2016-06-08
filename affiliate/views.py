from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MemberService import MembersService
from services.AffiliateService import AffiliateService
from django.views.decorators.http import require_http_methods
from services.IdentityDocumentTypeService import IdentityDocumentTypeService
from services.UbigeoService import UbigeoService
from Adapters.FormValidator import FormValidator
from .forms import  AffiliateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def affiliate_index(request):

    id_member = request.POST['id']

    member_service = MembersService()

    affiliate_service = AffiliateService()

    member = member_service.getMember(id_member)

    filter_affiliate = {}

    filter_affiliate["member"] = member

    affiliates = affiliate_service.filter(filter_affiliate)

    context = {
        'id_member' : id_member,
        'affiliates' : affiliates,
    }

    return render(request, 'Admin/Affiliates/index_affiliates.html', context) 


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def create_index(request):

    id_member = request.POST['id']

    ubigeo_service = UbigeoService()

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    departments = ubigeo_service.distinctDepartment()

    context = {
        'id_member': id_member,
        'ubigeo': ubigeo,
        'departments': doc_types
    }

    return render(request, 'Admin/Affiliates/new_affiliate.html', context)



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def create_affiliate(request):

    form = AffiliateForm(request.POST)

    id_member = request.POST['id_member']

    ubigeo_service = UbigeoService()

    identity_doc_type = request.POST['identity_document_type']

    if FormValidator.validateForm(form, request):

        identity_document_type_service = IdentityDocumentTypeService()

        doc_types = identity_document_type_service.getIdentityDocumentTypes()

        ubigeo = ubigeo_service.getAllUbigeo()

        context = {
            'id_member': id_member,
            'ubigeo': ubigeo,
            'doc_types': doc_types
        }

        return render(request, 'Admin/Members/new_affiliate.html', context)

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

        edit_data["member_id"] = id_member

        id_ubigeo = request.POST['district']

        ubi = ubigeo_service.getUbigeoById(id_ubigeo)

        edit_data["ubigeo"] = ubi

        affilliate_service = AffiliateService()

        affiliate_service.create(edit_data)

        member_service = MembersService()

        member = member_service.getMember(id_member)

        filter_affiliate = {}

        filter_affiliate["member"] = member

        affiliates = affiliate_service.filter(filter_affiliate)

        context = {
            'id_member' : id_member,
            'affiliates' : affiliates,
        }

        return render(request, 'Admin/Affiliates/index_affiliates.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_affiliate_index(request):

    id_affiliate = request.POST['id']

    affiliate_service = AffiliateService()

    affiliate = affiliate_service.getAffiliate(id_affiliate)

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
        'affiliate' : affiliate,
        'departments' : departments,
        'provinces' : provinces,
        'districts' : districts,
        'doc_types': doc_types,
    }

    return render(request, 'Admin/Affiliates/edit_affiliate.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_affiliate(request):

    form = AffiliateForm(request.POST)

    id_edit = request.POST['id']

    ubigeo_service = UbigeoService()

    identity_doc_type = request.POST['identity_document_type']

    if FormValidator.validateForm(form, request):

        affiliate_service = AffiliateService()

        affiliate = affiliate_service.getAffiliate(id_edit)

        identity_document_type_service = IdentityDocumentTypeService()

        doc_types = identity_document_type_service.getIdentityDocumentTypes()

        ubigeo = ubigeo_service.getAllUbigeo()

        context = {
            'affiliate': affiliate,
            'ubigeo': ubigeo,
            'doc_types': doc_types
        }

        return render(request, 'Admin/Affiliates/edit_affiliatehtml', context)

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

        id_ubigeo = request.POST['district']

        ubi = ubigeo_service.getUbigeoById(id_ubigeo)

        edit_data["ubigeo"] = ubi

        affilliate_service = AffiliateService()

        affiliate_service.update(id_edit, edit_data)

        affiliate = affiliate_service.getAffiliate(id_edit)

        id_member = affiliate.member.id

        affiliates = affiliate_service.filter(member=affiliate.member)

        context = {
            'id_member' : id_member,
            'affiliates' : affiliates,
        }

        return render(request, 'Admin/Affiliates/index_affiliates.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def delete_affiliate(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["state"] = 0

    affiliate_service = AffiliateService()

    affiliate_service.update(id_edit, edit_data)

    affiliate = affiliate_service.getAffiliate(id_edit)

    id_member = affiliate.member.id

    affiliates = affiliate_service.filter(member=member)

    context = {
        'id_member' : id_member,
        'affiliates' : affiliates,
    }

    return render(request, 'Admin/Affiliates/index_affiliates.html', context)
