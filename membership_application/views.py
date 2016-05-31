from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MembershipTypeService import MembershipTypeService
from services.IdentityDocumentTypeService import IdentityDocumentTypeService
from services.ObjectionService import ObjectionsService
from django.views.decorators.http import require_http_methods
from datetime import datetime
from Adapters.FormValidator import FormValidator
from .forms import MembershipApplicationForm
from objection import forms as oforms


#ADMIN

@require_http_methods(['GET'])
def index(request):

    member_application_service = Membership_ApplicationService()

    membershipApplications = member_application_service.getMembership_Applications()

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    context = {
        'membershipApplications' : membershipApplications,
        'doc_types' : doc_types,
    }

    return render(request, 'Admin/Membership/index_membership_request.html', context) 


@require_http_methods(['POST'])
def filter(request):

    member_application_service = Membership_ApplicationService()

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    filter_member_application = {}

    appStatus = request.POST['status']

    iniDate = request.POST['initialDate']

    endDate = request.POST['finalDate']

    num_doc = request.POST['num_doc']

    type_identity_doc = request.POST['identity_document_type']

    if iniDate != '':
        filter_member_application["initialDate"] = datetime.strptime(iniDate, '%m/%d/%Y')

    if endDate != '':
        filter_member_application["finalDate"] = datetime.strptime(endDate, '%m/%d/%Y')

    if num_doc != '':
        filter_member_application["document_number"] = num_doc

    if appStatus != '3':
        filter_member_application["status"] = appStatus

    if type_identity_doc != 'Todos':
        filter_member_application["identity_document_type"] = type_identity_doc

    membershipApplications = member_application_service.filter(filter_member_application)

    context = {
        'membershipApplications' : membershipApplications,
        'doc_types' : doc_types
    }

    return render(request, 'Admin/Membership/index_membership_request.html', context) 


@require_http_methods(['GET'])
def create_index(request):

    membership_type_service = MembershipTypeService()

    identity_document_type_service = IdentityDocumentTypeService()

    types = membership_type_service.getMembershipTypes()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    context = {

        'types' : types,
        'doc_types': doc_types,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Membership/new_membership_request.html', context)

@require_http_methods(['POST'])
def edit_index(request):

    membership_type_service = MembershipTypeService()

    identity_document_type_service = IdentityDocumentTypeService()

    types = membership_type_service.getMembershipTypes()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    member_application_service = Membership_ApplicationService()

    membershipId = request.POST['id']

    membership_application = member_application_service.getMembership_Application(membershipId)

    membership_application.initialDate = datetime.strftime(membership_application.initialDate, '%m/%d/%Y')

    membership_application.finalDate = datetime.strftime(membership_application.finalDate, '%m/%d/%Y')

    context = {
        'types' : types,
        'doc_types' : doc_types,
        'membership_application' : membership_application,
    }

    return render(request, 'Admin/Membership/edit_membership_request.html', context)

@require_http_methods(['POST'])
def delete_membership_application(request):

    insert_data = {}

    id_application = request.POST['id']

    insert_data["status"] = 0

    member_application_service = Membership_ApplicationService()

    member_application_service.update(id_application, insert_data)

    return HttpResponseRedirect(reverse('membership_application:index'))


@require_http_methods(['POST'])
def create_membership_application(request):

    membership_id = request.POST['membership_type']

    identity_document_id = request.POST['identity_document_type']

    form = MembershipApplicationForm(request.POST)

    request = FormValidator.validateForm(form, request)

    if not request:

        insert_data = {}

        insert_data["membership_type_id"] = membership_id

        insert_data["identity_document_type_id"] = identity_document_id

        insert_data["firstName"] = form.cleaned_data['firstName']

        insert_data["lastName"] = form.cleaned_data['lastName']

        insert_data["comments"] = form.cleaned_data['comments']

        insert_data["document_number"] = form.cleaned_data['num_doc']

        insert_data["initialDate"] = form.cleaned_data['initialDate']

        insert_data["finalDate"] = form.cleaned_data['finalDate']

        insert_data["status"] = 1

        member_application_service = Membership_ApplicationService()

        member_application_service.create(insert_data)

        return HttpResponseRedirect(reverse('membership_application:index'))

    else:
        membership_type_service = MembershipTypeService()

        identity_doc_type_service = IdentityDocumentTypeService()

        types = membership_type_service.getMembershipTypes()

        doc_types = identity_doc_type_service.getIdentityDocumentTypes()

        context = {
            'types' : types,
            'doc_types' : doc_types,
            'titulo': 'titulo'
        }

        return render(request, 'Admin/Membership/new_membership_request.html', context)


@require_http_methods(['POST'])
def edit_membership_application(request):

    form = MembershipApplicationForm(request.POST)

    id_application = request.POST['id']

    membership_type_id = request.POST['membership_type']

    identity_document_id = request.POST['identity_document_type']

    request = FormValidator.validateForm(form, request)    

    if not request:

        insert_data = {}

        insert_data["membership_type_id"] = membership_type_id

        insert_data["identity_document_type_id"] = identity_document_id

        insert_data["firstName"] = form.cleaned_data['firstName']

        insert_data["lastName"] = form.cleaned_data['lastName']

        insert_data["comments"] = form.cleaned_data['comments']

        insert_data["document_number"] = form.cleaned_data['num_doc']

        insert_data["initialDate"] = form.cleaned_data['initialDate']

        insert_data["finalDate"] = form.cleaned_data['finalDate']

        member_application_service = Membership_ApplicationService()

        member_application_service.update(id_application, insert_data)

        return HttpResponseRedirect(reverse('membership_application:index'))

    else:
        membership_type_service = MembershipTypeService()

        identity_doc_type_service = IdentityDocumentTypeService()

        member_application_service = Membership_ApplicationService()

        types = membership_type_service.getMembershipTypes()

        doc_types = identity_doc_type_service.getIdentityDocumentTypes()

        membership_application = member_application_service.getMembership_Application(id_application)

        membership_application.initialDate = datetime.strftime(membership_application.initialDate, '%m/%d/%Y')

        membership_application.finalDate = datetime.strftime(membership_application.finalDate, '%m/%d/%Y')

        context = {
            'types': types,
            'doc_types': doc_types,
            'membership_application': membership_application,
        }

        return render(request, 'Admin/Membership/edit_membership_request.html', context)


#USUARIO

@require_http_methods(['GET'])
def user_index(request):

    member_application_service = Membership_ApplicationService()

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    membershipApplications = member_application_service.getMembership_Applications()

    context = {
        'membershipApplications' : membershipApplications,
        'doc_types' : doc_types,
    }

    return render(request, 'index_membership_request.html', context) 


@require_http_methods(['POST'])
def user_filter(request):

    member_application_service = Membership_ApplicationService()

    identity_document_type_service = IdentityDocumentTypeService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    filter_member_application = {}

    filter_member_application["status"] = 1 

    lastName = request.POST['lastName']

    firstName = request.POST['firstName']

    num_doc = request.POST['num_doc']

    type_identity_doc = request.POST['identity_document_type']

    if lastName != '':
        filter_member_application["lastName"] = lastName

    if firstName != '':
        filter_member_application["firstName"] = firstName

    if num_doc != '':
        filter_member_application["document_number"] = num_doc

    if type_identity_doc != 'Todos':
        filter_member_application["identity_document_type"] = type_identity_doc

    membershipApplications = member_application_service.filter(filter_member_application)

    context = {
        'membershipApplications' : membershipApplications,
        'doc_types' : doc_types,
    }

    return render(request, 'index_membership_request.html', context) 


#OBJECIONES

@require_http_methods(['POST'])
def create_objection(request):

    form = oforms.ObjectionForm(request.POST)

    requestId = request.POST['id_membership']

    comments = request.POST['comments']

    request = FormValidator.validateForm(form, request)


    if not request:

        insert_data = {}

        insert_data["comments"] = comments

        insert_data["membership_application_id"] = requestId

        objection_service = ObjectionsService()

        objection_service.create(insert_data)

        return HttpResponseRedirect(reverse('membership_application:user_index'))

    else:
        member_application_service = Membership_ApplicationService()

        membership_application = member_application_service.getMembership_Application(requestId)

        context = {
            'membership_application': membership_application,
        }

        return render(request, 'Objections_members.html', context)


@require_http_methods(['POST'])
def objection_index(request):

    member_application_service = Membership_ApplicationService()

    requestId = request.POST['id']

    membership_application = member_application_service.getMembership_Application(requestId)

    context = {
        'membership_application' : membership_application,
    }

    return render(request, 'Objections_members.html', context)


@require_http_methods(['POST'])
def approve_membership_application(request):

    id_application = request.POST['id']

    member_application_service = Membership_ApplicationService()

    identity_doc_type_service = IdentityDocumentTypeService()

    doc_types = identity_doc_type_service.getIdentityDocumentTypes()

    membership_application =  member_application_service.getMembership_Application(id_application)

    context = {
        'titulo' : 'titulo',
        'doc_types' : doc_types,
        'membership_application' : membership_application,
    }

    return render(request, 'Admin/Membership/new_membership_member.html', context)


