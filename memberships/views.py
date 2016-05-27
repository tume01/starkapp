from django.template import loader
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MembershipTypeService import MembershipTypeService
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MembershipService import MembershipService
from services.ObjectionService import ObjectionsService
from services.MemberService import MembersService
from services.UsersService import UsersService
from datetime import datetime
from django.views.decorators.http import require_http_methods
from Adapters.FormValidator import FormValidator
from .forms import MembershipTypeForm
from .forms import MembershipForm
from members import forms as mForms
from users import forms as uForms


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

    membership_service = MembershipService()

    filter_data = {}

    filter_data["membership_type_id"] = id_edit

    filter_data["status"] = 1

    members = membership_service.filter(filter_data)

    print("Members:")
    print(members)

    if (len(members) == 0):

        membership_type_service = MembershipTypeService()

        membership_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('memberships:type/index'))


@require_http_methods(['POST'])
def create_membership_type(request):

    form = MembershipTypeForm(request.POST)

    request = FormValidator.validateForm(form, request)

    if not request:

        insert_data = {}

        insert_data["name"] = form.cleaned_data['name']

        insert_data["guests"] = form.cleaned_data['guests']

        insert_data["price"] = form.cleaned_data['price']

        insert_data["billing"] = form.cleaned_data['billing']

        insert_data["status"] = 1

        membership_type_service = MembershipTypeService()

        membership_type_service.create(insert_data)

        return HttpResponseRedirect(reverse('memberships:type/index'))

    else:

        context = {
            'titulo' : 'titulo'
        }
    
        return render(request, 'Admin/Membership/new_type_membership.html', context)


@require_http_methods(['POST'])
def edit_membership_type(request):

    form = MembershipTypeForm(request.POST)

    id_edit = request.POST['id']

    membership_type_service = MembershipTypeService()

    if FormValidator.validateForm(form, request):

        membership_type = membership_type_service.getType(id_edit)

        context = {
            'membershipType' : membership_type,
        }

        return render(request, 'Admin/Membership/edit_type_membership.html', context)

    else:

        edit_data = {}

        edit_data["name"] = form.cleaned_data['name']

        edit_data["guests"] = form.cleaned_data['guests']

        edit_data["price"] = form.cleaned_data['price']

        edit_data["billing"] = form.cleaned_data['billing']
        
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

    form = MembershipForm(request.POST)
    form2 = mForms.MemberForm(request.POST)

    membershipApplicationId = request.POST['id']

    if (not FormValidator.validateForm(form,request)
        and not FormValidator.validateForm(form2,request)):

        #Datos del membresia

        insert_data = {}

        insert_data["initialDate"] =  form.cleaned_data['initialDate']

        insert_data["finalDate"] =  form.cleaned_data['finalDate']

        insert_data["status"] = 1

        insert_data["membership_type_id"] = request.POST['membership_type_id']

        membership_service = MembershipService()

        membership = membership_service.create(insert_data)

        #Datos del usuario

        insert_data = {}

        insert_data["name"] = form2.cleaned_data['dni']

        insert_data["password"] = 1111

        insert_data["user_type_id"] = 1

        user_service = UsersService()

        user = user_service.create(insert_data)

        #Datos del miembro

        insert_data = {}

        insert_data["user_id"] = user.id

        insert_data["membership_id"] = membership.id

        insert_data["name"] = form2.cleaned_data['name']

        insert_data["surname"] = form2.cleaned_data['surname']

        insert_data["dni"] = form2.cleaned_data['dni']

        insert_data["phone"] = form2.cleaned_data['phone']

        insert_data["address"] = form2.cleaned_data['address']

        insert_data["email"] = form2.cleaned_data['email']

        insert_data["state"] = 1

        member_service = MembersService()

        member_service.create(insert_data)

        #Elimino solicitud

        id_application = membershipApplicationId

        insert_data = {}

        insert_data["status"] = 0

        member_application_service = Membership_ApplicationService()

        member_application_service.update(id_application, insert_data)

        return HttpResponseRedirect(reverse('membership_application:index'))

    else:
        member_application_service = Membership_ApplicationService()

        membershipApplication = member_application_service.getMembership_Application(membershipApplicationId)
    
        context = {
            'titulo': 'titulo',
            'membership_application': membershipApplication,
        }

        return render(request, 'Admin/Membership/new_membership_member.html', context)





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

    form = MembershipForm(request.POST)

    id_edit = request.POST['id']

    membership_service = MembershipService()

    if FormValidator.validateForm(form, request):

        membership_type_service = MembershipTypeService()

        membership = membership_service.getType(id_edit)

        types = membership_type_service.getMembershipTypes()

        context = {
            'membership': membership,
            'types' : types,
        }

        return render(request, 'Admin/Membership/edit_membership.html', context)

    else:

        edit_data = {}

        edit_data["initialDate"] = form.cleaned_data['initialDate']

        edit_data["finalDate"] = form.cleaned_data['finalDate']

        edit_data["membership_type_id"] = request.POST['membership_type_id']

        membership_service.update(id_edit, edit_data)

        return HttpResponseRedirect(reverse('members:index'))

