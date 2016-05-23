from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.Membership_ApplicationService import Membership_ApplicationService
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST'])
def filter(request):

    member_application_service = Membership_ApplicationService()

    filter_member_application = {}

    filter_member_application["iniDate"] = request.POST['iniDate']

    filter_member_application["endDate"] = request.POST['endDate']

    filter_member_application["dni"] = request.POST['dni']

    membershipApplications = member_application_service.getMembership_Applications(filter_member_application)

    context = {
        'membershipApplications' : membershipApplications,
    }

    return render(request, 'Admin/Membership/index_membership_request.html', context) 

@require_http_methods(['GET'])
def index(request):

    member_application_service = Membership_ApplicationService()

    membershipApplications = member_application_service.getMembership_Applications()

    context = {
        'membershipApplications' : membershipApplications,
    }

    return render(request, 'Admin/Membership/index_membership_request.html', context) 

@require_http_methods(['GET'])
def index_user(request):

    member_application_service = Membership_ApplicationService()

    membershipApplications = member_application_service.getMembership_Applications()

    context = {
        'membershipApplications' : membershipApplications,
    }

    return render(request, 'index_membership_request.html', context) 

@require_http_methods(['POST'])
def filter_user(request):

    member_application_service = Membership_ApplicationService()

    filter_member_application = {}

    filter_member_application["iniDate"] = request.POST['iniDate']

    filter_member_application["endDate"] = request.POST['endDate']

    filter_member_application["dni"] = request.POST['dni']

    membershipApplications = member_application_service.getMembership_Applications(filter_member_application)

    context = {
        'membershipApplications' : membershipApplications,
    }

    return render(request, 'index_membership_request.html', context) 


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Membership/new_membership_request.html', context)

@require_http_methods(['POST'])
def edit_index(request):

    member_application_service = Membership_ApplicationService()

    membershipId = request.POST['id']

    membership_application = member_application_service.getMembership_Application(membershipId)

    context = {
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

    return HttpResponseRedirect(reverse('requests:index'))


@require_http_methods(['POST'])
def create_membership_application(request):

    insert_data = {}

    insert_data["name"] = request.POST['name']

    insert_data["comments"] = request.POST['comments']

    insert_data["dni"] = request.POST['dni']

    insert_data["iniDate"] = request.POST['iniDate']

    insert_data["endDate"] = request.POST['endDate']

    insert_data["status"] = 1

    member_application_service = Membership_ApplicationService()

    member_application_service.create(insert_data)

    return HttpResponseRedirect(reverse('mebership_application:index'))


@require_http_methods(['POST'])
def edit_membership_application(request):

    insert_data = {}

    insert_data["name"] = request.POST['name']

    insert_data["dni"] = request.POST['dni']

    insert_data["comments"] = request.POST['comments']

    insert_data["iniDate"] = request.POST['iniDate']

    insert_data["endDate"] = request.POST['endDate']

    id_application = request.POST['id']

    member_application_service = Membership_ApplicationService()

    member_application_service.update(id_application, insert_data)

    return HttpResponseRedirect(reverse('mebership_application:index'))


@require_http_methods(['POST'])
def create_objection(request):

    insert_data = {}

    insert_data["comments"] = request.POST['comments']

    id_application = request.POST['id']

    #objection_service = ObjectionService()

    #objection_service.create(id_application, insert_data)

    return HttpResponseRedirect(reverse('mebership_application:index'))


@require_http_methods(['POST'])
def objection_index(request):

    member_application_service = Membership_ApplicationService()

    requestId = request.POST['id']

    membership_application = member_application_service.getRequest(requestId)

    context = {
        'membership_application' : membership_application,
    }

    return HttpResponseRedirect(reverse('mebership_application:index'))