from django.template import loader
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.MembershipTypeService import MembershipTypeService
from services.Membership_ApplicationService import Membership_ApplicationService
from services.IdentityDocumentTypeService import IdentityDocumentTypeService
from services.MembershipService import MembershipService
from services.SuspensionService import SuspensionService
from services.ObjectionService import ObjectionsService
from services.UbigeoService import UbigeoService
from services.MemberService import MembersService
from services.RelationshipService import RelationshipService
from services.AffiliateService import AffiliateService
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.views.decorators.http import require_http_methods
from adapters.FormValidator import FormValidator
from .forms import MembershipTypeForm
from .forms import MembershipForm
from membership_application import forms as apForms
from members import forms as mForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['GET'])
def membership_type_index(request):

    membership_type_service = MembershipTypeService()

    types = membership_type_service.getMembershipTypes()

    context = {
        'membershipTypes' : types,
    }

    return render(request, 'Admin/Membership/index_type_membership.html', context) 


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['GET'])
def create_membership_type_index(request):

    context = {
        'titulo' : 'titulo'
    }
    
    return render(request, 'Admin/Membership/new_type_membership.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_membership_type_index(request):

    membership_type_service = MembershipTypeService()

    typeId = request.POST['id']

    type = membership_type_service.getType(typeId)

    context = {
        'membershipType' : type,
    }

    return render(request, 'Admin/Membership/edit_type_membership.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def delete_membership_type(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    membership_service = MembershipService()

    membership_application_service = Membership_ApplicationService()

    filter_data = {}

    filter_data["membership_type_id"] = id_edit

    filter_data["status"] = 1

    members = membership_service.filter(filter_data)

    membership_applications = membership_application_service.filter(filter_data)

    if (len(members) == 0 and len(membership_applications) == 0):

        membership_type_service = MembershipTypeService()

        membership_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('memberships:type/index'))


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
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



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
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



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def membership_accept(request):

    application_id = request.POST['id']

    objection_service = ObjectionsService()

    objections = objection_service.getObjectionByApplicationId(application_id)

    member_application_service = Membership_ApplicationService()

    membership_application =  member_application_service.getMembership_Application(application_id)


    context = {
        'objections' : objections,
        'membership_application' : membership_application,
        'id' : application_id,
    }

    return render(request, 'Admin/Membership/index_membership_approval.html', context)



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def create_membership(request):

    form = MembershipForm(request.POST)
    form2 = mForms.MemberForm(request.POST)
    form3 = apForms.MembershipApplicationForm(request.POST)

    membershipApplicationId = request.POST['id']

    if (not FormValidator.validateForm(form,request)
        and not FormValidator.validateForm(form2,request)
        and not FormValidator.validateForm(form3, request)):

        #Datos del membresia

        insert_data = {}

        insert_data["initialDate"] =  form.cleaned_data['initialDate']

        insert_data["finalDate"] =  form.cleaned_data['finalDate']

        insert_data["status"] = 1

        insert_data["membership_type_id"] = request.POST['membership_type_id']

        membership_service = MembershipService()

        membership = membership_service.create(insert_data)

        #Datos del usuario

        password = get_random_string(length=10)

        email = EmailMessage('Bienvenido al club' ,
                             'Hola ' + form2.cleaned_data['name'] + ',\n\nTe damos la bienvenida al club.'+
                             '\n\n\nPara poder acceder al sistema utiliza los siguientes datos: '+
                             '\nUsuario:    '+ str(form2.cleaned_data['num_doc']) +
                             '\nContraseña: '+ str(password), 
                             to=[form2.cleaned_data['email']])

        email.send()

        user = User.objects.create_user(username=form2.cleaned_data['num_doc'], email=form2.cleaned_data['email'],   password=password, first_name=form2.cleaned_data['name'], last_name=form2.cleaned_data['paternalLastName'])

        group = Group.objects.get(name='usuarios')

        group.user_set.add(user)
    

        #Datos del miembro

        insert_data = {}

        insert_data["user_id"] = user.id

        insert_data["membership_id"] = membership.id

        insert_data['identity_document_type_id'] = request.POST['identity_document_type']

        insert_data["name"] = form2.cleaned_data['name']

        insert_data["paternalLastName"] = form2.cleaned_data['paternalLastName']

        insert_data["maternalLastName"] = form2.cleaned_data['maternalLastName']

        insert_data["document_number"] = form2.cleaned_data['num_doc']

        insert_data["phone"] = form2.cleaned_data['phone']

        insert_data["address"] = form2.cleaned_data['address']

        insert_data["email"] = form2.cleaned_data['email']

        insert_data["state"] = 1

        ubigeo_service = UbigeoService()

        filter_ubigeo = {}

        filter_ubigeo["department"] = request.POST['department']

        filter_ubigeo["province"] = request.POST['province']

        filter_ubigeo["district"] = request.POST['district']

        ubi = ubigeo_service.filter(filter_ubigeo)

        insert_data["ubigeo"] = ubi[0]

        insert_data["photo"] = request.FILES['photo']

        insert_data["gender"] = request.POST['gender']

        insert_data["workPlace"] = form2.cleaned_data['workPlace']

        insert_data["workPlaceJob"] = form2.cleaned_data['workPlaceJob']

        insert_data["workPlacePhone"] = form2.cleaned_data['workPlacePhone']

        insert_data["nationality"] = form2.cleaned_data['nationality']

        insert_data["martialStatus"] = form2.cleaned_data['maritalStatus']

        insert_data["cellphoneNumber"] = form2.cleaned_data['cellphoneNumber']

        insert_data["specialization"] = form2.cleaned_data['specialization']

        insert_data["birthDate"] = form2.cleaned_data['birthDate']

        insert_data["birthPlace"] = form2.cleaned_data['birthPlace']

        filter_ubigeo["department"] = request.POST['birthDepartment']

        filter_ubigeo["province"] = request.POST['birthProvince']

        filter_ubigeo["district"] = request.POST['birthDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        insert_data["birthUbigeo"] = ubi[0]

        member_service = MembersService()

        newmember = member_service.create(insert_data)

        #En caso se halla registrado un conyuge se agrega como afiliado

        spouseName = form3.cleaned_data['sfirstName']

        if spouseName != '':

            insert_affiliate = {}

            insert_affiliate["member"] = newmember

            insert_affiliate["name"] = spouseName

            insert_affiliate["identity_document_type_id"] = request.POST['sidentity_document_id']

            insert_affiliate["paternalLastName"] = form.cleaned_data['spaternalLastName']

            insert_affiliate["maternalLastName"] = form.cleaned_data['smaternalLastName']

            insert_affiliate["document_number"] = form.cleaned_data['snum_doc']

            insert_affiliate["phone"] = form2.cleaned_data['phone']

            insert_affiliate["address"] = form2.cleaned_data['address']

            insert_affiliate["gender"] = request.POST['sgender']

            insert_affiliate["specialization"] = form.cleaned_data['sspecialization']

            insert_affiliate["nationality"] = form.cleaned_data['snationality']

            insert_affiliate["birthDate"] = request.POST['sbirthDate']

            insert_affiliate["birthPlace"] = form.cleaned_data['sbirthPlace']

            insert_affiliate['maritalStatus'] = 'casado'

            filter_ubigeo["department"] = request.POST['sbirthDepartment']

            filter_ubigeo["province"] = request.POST['sbirthProvince']

            filter_ubigeo["district"] = request.POST['sbirthDistrict']

            ubi = ubigeo_service.filter(filter_ubigeo)

            insert_affiliate["birthUbigeo"] = ubi[0]

            insert_affiliate["photo"] = request.FILES['sphoto']

            insert_affiliate["workPlace"] = form.cleaned_data['sworkPlace']

            insert_affiliate["workPlaceJob"] = form.cleaned_data['sworkPlaceJob']

            insert_affiliate["workPlacePhone"] = request.POST['sworkPlacePhone']

            insert_affiliate["email"] = form.cleaned_data['semail']

            insert_affiliate["state"] = 1

            relationship_service = RelationshipService()

            filter_relationship = {}

            filter_relationship['description'] = 'Cónyuge'

            relationships = relationship_service.filter(filter_relationship)

            insert_affiliate['relationship'] = relationships[0]

            affiliate_service = AffiliateService()

            affiliate_service.create(insert_affiliate)

        #Elimino solicitud (se pone como aceptada)

        id_application = membershipApplicationId

        insert_data = {}

        insert_data["status"] = 2

        member_application_service = Membership_ApplicationService()

        member_application_service.update(id_application, insert_data)

        return HttpResponseRedirect(reverse('membership_application:index'))

    else:
        member_application_service = Membership_ApplicationService()

        identity_doc_type_service = IdentityDocumentTypeService()

        doc_types = identity_doc_type_service.getIdentityDocumentTypes()

        membershipApplication = member_application_service.getMembership_Application(membershipApplicationId)
    
        context = {
            'titulo': 'titulo',
            'doc_types' : doc_types,
            'membership_application': membershipApplication,
        }

        return render(request, 'Admin/Membership/new_membership_member.html', context)




@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def membership_edit_index(request):

    membership_service = MembershipService()

    memberId = request.POST['id']

    member_service = MembersService()

    member = member_service.getMember(memberId)

    membership = member.membership

    membership.initialDate = datetime.strftime(membership.initialDate, '%m/%d/%Y')

    membership.finalDate = datetime.strftime(membership.finalDate, '%m/%d/%Y')

    membership_type_service = MembershipTypeService()

    types = membership_type_service.getMembershipTypes()

    context = {
        'membership' : membership,
        'types' : types,
    }

    return render(request, 'Admin/Membership/edit_membership.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def membership_edit(request):

    form = MembershipForm(request.POST)

    id_edit = request.POST['id']

    membership_service = MembershipService()

    if FormValidator.validateForm(form, request):

        membership_type_service = MembershipTypeService()

        membership = membership_service.getMembership(id_edit)

        membership.initialDate = datetime.strftime(membership.initialDate, '%m/%d/%Y')

        membership.finalDate = datetime.strftime(membership.finalDate, '%m/%d/%Y')
        
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

#user		
@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')	
def membership_show(request):

	user = request.user
    
	member_service = MembersService()
	filter = {}
	filter["user"] =user
	member = member_service.filter(filter)
	context = {
		'membership' : member[0].membership
	}
	return render(request, 'User/membership.html',context)
	

	
