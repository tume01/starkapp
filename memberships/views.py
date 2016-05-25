from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MembershipTypeService import MembershipTypeService
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MembershipService import MembershipService
from services.ObjectionService import ObjectionsService
from services.MemberService import MembersService
from datetime import datetime
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def membership_type_index(request):

    membership_type_service = MembershipTypeService()

    types = membership_type_service.getMembershipTypes()

    context = {
        'membershipTypes' : types,
    }

    return render(request, 'Admin/Membership/index_type_membership.html', context) 


@require_http_methods(['GET'])
def create_membership_type_index(request):

    context = {
        'titulo' : 'titulo'
    }
    
    return render(request, 'Admin/Membership/new_type_membership.html', context)

@require_http_methods(['POST'])
def edit_membership_type_index(request):

    membership_type_service = MembershipTypeService()

    typeId = request.POST['id']

    type = membership_type_service.getType(typeId)

    context = {
        'membershipType' : type,
    }

    return render(request, 'Admin/Membership/edit_type_membership.html', context)


@require_http_methods(['POST'])
def delete_membership_type(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    membership_type_service = MembershipTypeService()

    membership_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('memberships:type/index'))


@require_http_methods(['POST'])
def create_membership_type(request):

    insert_data = {}

    insert_data["name"] = request.POST['name']

    insert_data["guests"] = request.POST['guests']

    insert_data["price"] = request.POST['price']

    insert_data["billing"] = request.POST['billing']

    insert_data["status"] = 1

    membership_type_service = MembershipTypeService()

    membership_type_service.create(insert_data)

    return HttpResponseRedirect(reverse('memberships:type/index'))


@require_http_methods(['POST'])
def edit_membership_type(request):

    edit_data = {}

    edit_data["name"] = request.POST['name']

    edit_data["guests"] = request.POST['guests']

    edit_data["price"] = request.POST['price']

    edit_data["billing"] = request.POST['billing']

    id_edit = request.POST['id']

    membership_type_service = MembershipTypeService()

    membership_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('memberships:type/index'))


@require_http_methods(['POST'])
def membership_accept(request):

    application_id = request.POST['id']

    insert_data = {}

    objection_service = ObjectionsService()

    objections = objection_service.getObjectionByApplicationId(application_id)

    context = {
        'objections' : objections,
        'id' : application_id,
    }

    return render(request, 'Admin/Membership/index_membership_approval.html', context)



@require_http_methods(['POST'])
def create_membership(request):

    #Datos de la membresia

    insert_data = {}

    insert_data["initialDate"] =  datetime.strptime(request.POST['initialDate'], '%m/%d/%Y')

    insert_data["finalDate"] =  datetime.strptime(request.POST['finalDate'], '%m/%d/%Y')

    insert_data["status"] = 1

    insert_data["membership_type_id"] = request.POST['membership_type_id']

    membership_service = MembershipService()

    membership = membership_service.create(insert_data)

    #Datos del miembro

    insert_data = {}

    insert_data["membership_id"] = membership.id

    insert_data["name"] = request.POST['name']

    insert_data["surname"] = request.POST['surname']

    insert_data["dni"] = request.POST['dni']

    insert_data["phone"] = request.POST['phone']

    insert_data["address"] = request.POST['address']

    insert_data["email"] = request.POST['email']

    insert_data["state"] = 1

    member_service = MembersService()

    member_service.create(insert_data)

    #Elimino solicitud

    id_application = request.POST['id']

    insert_data = {}

    insert_data["status"] = 0

    member_application_service = Membership_ApplicationService()

    member_application_service.update(id_application, insert_data)

    return HttpResponseRedirect(reverse('membership_application:index'))


@require_http_methods(['POST'])
def membership_edit_index(request):

    membership_service = MembershipService()

    membershipId = request.POST['id']

    membership = membership_service.getMembership(membershipId)

    membership.initialDate = datetime.strftime(membership.initialDate, '%m/%d/%Y')

    membership.finalDate = datetime.strftime(membership.finalDate, '%m/%d/%Y')

    membership_type_service = MembershipTypeService()

    types = membership_type_service.getMembershipTypes()

    context = {
        'membership' : membership,
        'types' : types,
    }

    return render(request, 'Admin/Membership/edit_membership.html', context)


@require_http_methods(['POST'])
def membership_edit(request):

    edit_data = {}

    edit_data["initialDate"] =  datetime.strptime(request.POST['initialDate'], '%m/%d/%Y')

    edit_data["finalDate"] =  datetime.strptime(request.POST['finalDate'], '%m/%d/%Y')

    edit_data["membership_type_id"] = request.POST['membership_type_id']

    id_edit = request.POST['id']

    membership_service = MembershipService()

    membership_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('members:index'))