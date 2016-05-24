from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MembershipTypeService import MembershipTypeService
from services.ObjectionService import ObjectionsService
from django.views.decorators.http import require_http_methods
from datetime import datetime

#ADMIN

@require_http_methods(['GET'])
def index(request):

    member_application_service = Membership_ApplicationService()

    membershipApplications = member_application_service.getMembership_Applications()

    context = {
        'membershipApplications' : membershipApplications,
    }

    return render(request, 'Admin/Membership/index_membership_request.html', context) 


@require_http_methods(['POST'])
def filter(request):

    member_application_service = Membership_ApplicationService()

    filter_member_application = {}

    filter_member_application["status"] = 1 

    iniDate = request.POST['initialDate']

    endDate = request.POST['finalDate']

    dni = request.POST['dni']

    if iniDate != '':
        filter_member_application["initialDate"] = datetime.strptime(iniDate, '%m/%d/%Y')

    if endDate != '':
        filter_member_application["finalDate"] = datetime.strptime(endDate, '%m/%d/%Y')

    if dni != '':
        filter_member_application["dni"] = dni

    membershipApplications = member_application_service.filter(filter_member_application)

    context = {
        'membershipApplications' : membershipApplications,
    }

    return render(request, 'Admin/Membership/index_membership_request.html', context) 


@require_http_methods(['GET'])
def create_index(request):

    membership_type_service = MembershipTypeService()

    types = membership_type_service.getMembershipTypes()

    context = {

        'types' : types,

        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Membership/new_membership_request.html', context)

@require_http_methods(['POST'])
def edit_index(request):

    membership_type_service = MembershipTypeService()

    types = membership_type_service.getMembershipTypes()

    member_application_service = Membership_ApplicationService()

    membershipId = request.POST['id']

    membership_application = member_application_service.getMembership_Application(membershipId)

    membership_application.initialDate = datetime.strftime(membership_application.initialDate, '%m/%d/%Y')

    membership_application.finalDate = datetime.strftime(membership_application.finalDate, '%m/%d/%Y')

    context = {
        'types' : types,
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

    insert_data = {}
 
    insert_data["membership_type_id"] = request.POST['membership_type']

    insert_data["firstName"] = request.POST['firstName']

    insert_data["lastName"] = request.POST['lastName']

    insert_data["comments"] = request.POST['comments']

    insert_data["dni"] = request.POST['dni']

    insert_data["initialDate"] =  datetime.strptime(request.POST['initialDate'], '%m/%d/%Y')

    insert_data["finalDate"] =  datetime.strptime(request.POST['finalDate'], '%m/%d/%Y')

    insert_data["status"] = 1

    member_application_service = Membership_ApplicationService()

    member_application_service.create(insert_data)

    return HttpResponseRedirect(reverse('membership_application:index'))


@require_http_methods(['POST'])
def edit_membership_application(request):

    insert_data = {}

    insert_data["membership_type_id"] = request.POST['membership_type']

    insert_data["firstName"] = request.POST['firstName']

    insert_data["lastName"] = request.POST['lastName']

    insert_data["comments"] = request.POST['comments']

    insert_data["dni"] = request.POST['dni']

    insert_data["initialDate"] =  datetime.strptime(request.POST['initialDate'], '%m/%d/%Y')

    insert_data["finalDate"] = datetime.strptime(request.POST['finalDate'], '%m/%d/%Y')

    id_application = request.POST['id']

    member_application_service = Membership_ApplicationService()

    member_application_service.update(id_application, insert_data)

    return HttpResponseRedirect(reverse('membership_application:index'))


#USUARIO

@require_http_methods(['GET'])
def user_index(request):

    member_application_service = Membership_ApplicationService()

    membershipApplications = member_application_service.getMembership_Applications()

    context = {
        'membershipApplications' : membershipApplications,
    }

    return render(request, 'index_membership_request.html', context) 


@require_http_methods(['POST'])
def user_filter(request):

    member_application_service = Membership_ApplicationService()

    filter_member_application = {}

    filter_member_application["status"] = 1 

    lastName = request.POST['lastName']

    firstName = request.POST['firstName']

    dni = request.POST['dni']

    if lastName != '':
        filter_member_application["lastName"] = lastName

    if firstName != '':
        filter_member_application["firstName"] = firstName

    if dni != '':
        filter_member_application["dni"] = dni

    membershipApplications = member_application_service.filter(filter_member_application)

    context = {
        'membershipApplications' : membershipApplications,
    }

    return render(request, 'index_membership_request.html', context) 


#OBJECIONES

@require_http_methods(['POST'])
def create_objection(request):

    insert_data = {}

    insert_data["comments"] = request.POST['comments']

    insert_data["membership_application_id"] = request.POST['id_membership']

    objection_service = ObjectionsService()

    objection_service.create(insert_data)

    return HttpResponseRedirect(reverse('membership_application:user_index'))


@require_http_methods(['POST'])
def objection_index(request):

    member_application_service = Membership_ApplicationService()

    requestId = request.POST['id']

    membership_application = member_application_service.getMembership_Application(requestId)

    context = {
        'membership_application' : membership_application,
    }

    return render(request, 'Objections_members.html', context)