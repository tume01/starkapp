from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MembershipTypeService import MembershipTypeService
from services.MemberService import MembersService
from services.AffiliateService import AffiliateService
from services.IdentityDocumentTypeService import IdentityDocumentTypeService
from services.UbigeoService import UbigeoService
from services.ObjectionService import ObjectionsService
from django.views.decorators.http import require_http_methods
from datetime import datetime
from adapters.FormValidator import FormValidator
from .forms import MembershipApplicationForm
from objection import forms as oforms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib import messages

#ADMIN
@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
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


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
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
        filter_member_application["initialDate__gte"] = datetime.strptime(iniDate, '%d/%m/%Y')

    if endDate != '':
        filter_member_application["finalDate__lte"] = datetime.strptime(endDate, '%d/%m/%Y')

    if num_doc != '':
        filter_member_application["document_number__contains"] = num_doc

    if appStatus != '4':
        filter_member_application["status"] = appStatus

    if type_identity_doc != 'Todos':
        filter_member_application["identity_document_type"] = type_identity_doc

    membershipApplications = member_application_service.filter(filter_member_application)

    data = serializers.serialize("json", membershipApplications)

    return HttpResponse(data, content_type='application/json')
    

@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['GET'])
def create_index(request):

    membership_type_service = MembershipTypeService()

    ubigeo_service = UbigeoService()

    identity_document_type_service = IdentityDocumentTypeService()

    types = membership_type_service.getMembershipTypes()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    ubigeo = ubigeo_service.distinctDepartment()

    context = {

        'types' : types,
        'ubigeo' : ubigeo,
        'doc_types': doc_types,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Membership/new_membership_request.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_index(request):

    membership_type_service = MembershipTypeService()

    identity_document_type_service = IdentityDocumentTypeService()

    types = membership_type_service.getMembershipTypes()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    member_application_service = Membership_ApplicationService()

    membershipId = request.POST['id']

    membership_application = member_application_service.getMembership_Application(membershipId)

    ubigeo_service = UbigeoService()

    departments = ubigeo_service.distinctDepartment()

    filter_ubigeo = {}

    filter_ubigeo["department"] = membership_application.ubigeo.department

    provinces = ubigeo_service.distinctProvince(filter_ubigeo)

    filter_ubigeo["department"] = membership_application.birthUbigeo.department

    provinces2 = ubigeo_service.distinctProvince(filter_ubigeo)

    filter_ubigeo = {}

    filter_ubigeo["province"] = membership_application.ubigeo.province

    districts = ubigeo_service.distinctDistrict(filter_ubigeo)

    filter_ubigeo["province"] = membership_application.birthUbigeo.province

    districts2 = ubigeo_service.distinctDistrict(filter_ubigeo)

    context = {
        'types' : types,
        'doc_types' : doc_types,
        'departments': departments,
        'provinces': provinces,
        'districts': districts,
        'provincesBirth': provinces2,
        'districtsBirth': districts2,
        'membership_application' : membership_application,
    }

    if(membership_application.sbirthUbigeo):

        filter_ubigeo = {}

        filter_ubigeo["department"] = membership_application.sbirthUbigeo.department

        provinces3 = ubigeo_service.distinctProvince(filter_ubigeo)

        filter_ubigeo = {}

        filter_ubigeo["province"] = membership_application.sbirthUbigeo.province

        districts3 = ubigeo_service.distinctDistrict(filter_ubigeo)

        context.update({'provincesSpouse': provinces3, 'districtsSpouse': districts3,})

    return render(request, 'Admin/Membership/edit_membership_request.html', context)


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def delete_membership_application(request):

    insert_data = {}

    id_application = request.POST['id']

    insert_data["status"] = 0

    member_application_service = Membership_ApplicationService()

    member_application_service.update(id_application, insert_data)

    return HttpResponseRedirect(reverse('membership_application:index'))



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def create_membership_application(request):

    ubigeo_service = UbigeoService()

    membership_id = request.POST['membership_type']

    identity_document_id = request.POST['identity_document_type']

    sidentity_document_id = request.POST['sidentity_document_type']

    form = MembershipApplicationForm(request.POST, request.FILES)

    request2 = FormValidator.validateForm(form, request)

    if not request2:

        insert_data = {}

        insert_data["membership_type_id"] = membership_id

        insert_data["identity_document_type_id"] = identity_document_id

        insert_data["firstName"] = form.cleaned_data['firstName']

        insert_data["paternalLastName"] = form.cleaned_data['paternalLastName']

        insert_data["maternalLastName"] = form.cleaned_data['maternalLastName']

        insert_data["comments"] = form.cleaned_data['comments']

        insert_data["document_number"] = form.cleaned_data['num_doc']

        insert_data["initialDate"] = form.cleaned_data['initialDate']

        insert_data["finalDate"] = form.cleaned_data['finalDate']

        insert_data['address'] = form.cleaned_data['address']

        filter_ubigeo = {}

        filter_ubigeo["department"] = request.POST['addressDepartment']

        filter_ubigeo["province"] = request.POST['addressProvince']

        filter_ubigeo["district"] = request.POST['addressDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        insert_data["ubigeo"] = ubi[0]

        filter_ubigeo["department"] = request.POST['birthDepartment']

        filter_ubigeo["province"] = request.POST['birthProvince']

        filter_ubigeo["district"] = request.POST['birthDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        insert_data["birthUbigeo"] = ubi[0]

        insert_data["status"] = 1

        if 'photo' in request.FILES:

            insert_data["photo"] = request.FILES['photo']

        else:

            membership_type_service = MembershipTypeService()

            identity_doc_type_service = IdentityDocumentTypeService()

            types = membership_type_service.getMembershipTypes()

            doc_types = identity_doc_type_service.getIdentityDocumentTypes()

            ubigeo = ubigeo_service.distinctDepartment()

            context = {
                'types' : types,
                'doc_types' : doc_types,
                'ubigeo' : ubigeo,
                'titulo': 'titulo'
            }

            messages.error(request, 'Debe ingresar una foto')

            return render(request, 'Admin/Membership/new_membership_request.html', context)

        insert_data["gender"] = request.POST['gender']

        insert_data["workPlace"] = form.cleaned_data['workPlace']

        insert_data["workPlaceJob"] = form.cleaned_data['workPlaceJob']

        insert_data["workPlacePhone"] = form.cleaned_data['workPlacePhone']

        insert_data["nationality"] = form.cleaned_data['nationality']

        insert_data["maritalStatus"] = form.cleaned_data['maritalStatus']

        insert_data["cellphoneNumber"] = form.cleaned_data['cellphoneNumber']

        insert_data["specialization"] = form.cleaned_data['specialization']

        insert_data["birthDate"] = form.cleaned_data['birthDate']

        insert_data["birthPlace"] = form.cleaned_data['birthPlace']

        insert_data["email"] = form.cleaned_data['email']

        insert_data["phone"] = form.cleaned_data['phone']

        if form.cleaned_data['sfirstName'] != '' and form.cleaned_data['spaternalLastName'] != '':

            insert_data["sidentity_document_type_id"] = sidentity_document_id

            insert_data["sfirstName"] = form.cleaned_data['sfirstName']

            insert_data["spaternalLastName"] = form.cleaned_data['spaternalLastName']

            insert_data["smaternalLastName"] = form.cleaned_data['smaternalLastName']

            insert_data["sdocument_number"] = form.cleaned_data['snum_doc']

            insert_data["sgender"] = request.POST['sgender']

            insert_data["scellphoneNumber"] = form.cleaned_data['scellphoneNumber']

            insert_data["sspecialization"] = form.cleaned_data['sspecialization']

            insert_data["snationality"] = form.cleaned_data['snationality']

            insert_data["sbirthDate"] = form.cleaned_data['sbirthDate']

            insert_data["sbirthPlace"] = form.cleaned_data['sbirthPlace']

            filter_ubigeo["department"] = request.POST['sbirthDepartment']

            filter_ubigeo["province"] = request.POST['sbirthProvince']

            filter_ubigeo["district"] = request.POST['sbirthDistrict']

            ubi = ubigeo_service.filter(filter_ubigeo)

            insert_data["sbirthUbigeo"] = ubi[0]

            if 'sphoto' in request.FILES:

                insert_data["sphoto"] = request.FILES['sphoto']

            insert_data["sworkPlace"] = form.cleaned_data['sworkPlace']

            insert_data["sworkPlaceJob"] = form.cleaned_data['sworkPlaceJob']

            insert_data["sworkPlacePhone"] = request.POST['sworkPlacePhone']

            insert_data["semail"] = form.cleaned_data['semail']

        member_application_service = Membership_ApplicationService()

        member_application_service.create(insert_data)

        return HttpResponseRedirect(reverse('membership_application:index'))

    else:
        membership_type_service = MembershipTypeService()

        identity_doc_type_service = IdentityDocumentTypeService()

        types = membership_type_service.getMembershipTypes()

        doc_types = identity_doc_type_service.getIdentityDocumentTypes()

        ubigeo = ubigeo_service.distinctDepartment()

        context = {
            'types' : types,
            'doc_types' : doc_types,
            'ubigeo' : ubigeo,
            'titulo': 'titulo'
        }

        return render(request2, 'Admin/Membership/new_membership_request.html', context)



@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def edit_membership_application(request):

    sidentity_document_id = request.POST['sidentity_document_type']

    ubigeo_service = UbigeoService()

    form = MembershipApplicationForm(request.POST, request.FILES)

    id_application = request.POST['id']

    membership_type_id = request.POST['membership_type']

    identity_document_id = request.POST['identity_document_type']

    request2 = FormValidator.validateForm(form, request)

    if not request2:

        insert_data = {}

        insert_data["membership_type_id"] = membership_type_id

        insert_data["identity_document_type_id"] = identity_document_id

        insert_data["firstName"] = form.cleaned_data['firstName']

        insert_data["paternalLastName"] = form.cleaned_data['paternalLastName']

        insert_data["maternalLastName"] = form.cleaned_data['maternalLastName']

        insert_data["comments"] = form.cleaned_data['comments']

        insert_data["document_number"] = form.cleaned_data['num_doc']

        insert_data["initialDate"] = form.cleaned_data['initialDate']

        insert_data["finalDate"] = form.cleaned_data['finalDate']

        insert_data['address'] = form.cleaned_data['address']

        filter_ubigeo = {}

        filter_ubigeo["department"] = request.POST['addressDepartment']

        filter_ubigeo["province"] = request.POST['addressProvince']

        filter_ubigeo["district"] = request.POST['addressDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        insert_data["ubigeo"] = ubi[0]

        filter_ubigeo["department"] = request.POST['birthDepartment']

        filter_ubigeo["province"] = request.POST['birthProvince']

        filter_ubigeo["district"] = request.POST['birthDistrict']

        ubi = ubigeo_service.filter(filter_ubigeo)

        insert_data["birthUbigeo"] = ubi[0]

        insert_data["status"] = 1

        if 'photo' in request.FILES:
            
            insert_data["photo"] = request.FILES['photo']

        insert_data["gender"] = request.POST['gender']

        insert_data["workPlace"] = form.cleaned_data['workPlace']

        insert_data["workPlaceJob"] = form.cleaned_data['workPlaceJob']

        insert_data["workPlacePhone"] = form.cleaned_data['workPlacePhone']

        insert_data["nationality"] = form.cleaned_data['nationality']

        insert_data["martialStatus"] = form.cleaned_data['maritalStatus']

        insert_data["cellphoneNumber"] = form.cleaned_data['cellphoneNumber']

        insert_data["specialization"] = form.cleaned_data['specialization']

        insert_data["birthDate"] = form.cleaned_data['birthDate']

        insert_data["birthPlace"] = form.cleaned_data['birthPlace']

        insert_data["email"] = form.cleaned_data['email']

        insert_data["phone"] = form.cleaned_data['phone']

        if form.cleaned_data['sfirstName'] != '' and form.cleaned_data['spaternalLastName'] != '':

            insert_data["sidentity_document_type_id"] = sidentity_document_id

            insert_data["sfirstName"] = form.cleaned_data['sfirstName']

            insert_data["spaternalLastName"] = form.cleaned_data['spaternalLastName']

            insert_data["smaternalLastName"] = form.cleaned_data['smaternalLastName']

            insert_data["sdocument_number"] = form.cleaned_data['snum_doc']

            insert_data["sgender"] = request.POST['sgender']

            insert_data["sspecialization"] = form.cleaned_data['sspecialization']

            insert_data["snationality"] = form.cleaned_data['snationality']

            insert_data["sbirthDate"] = form.cleaned_data['sbirthDate']

            insert_data["sbirthPlace"] = form.cleaned_data['sbirthPlace']

            insert_data["scellphoneNumber"] = form.cleaned_data['scellphoneNumber']

            filter_ubigeo["department"] = request.POST['sbirthDepartment']

            filter_ubigeo["province"] = request.POST['sbirthProvince']

            filter_ubigeo["district"] = request.POST['sbirthDistrict']

            ubi = ubigeo_service.filter(filter_ubigeo)

            insert_data["sbirthUbigeo"] = ubi[0]

            if 'sphoto' in request.FILES:

                insert_data["sphoto"] = request.FILES['sphoto']
    
            insert_data["sworkPlace"] = form.cleaned_data['sworkPlace']

            insert_data["sworkPlaceJob"] = form.cleaned_data['sworkPlaceJob']

            insert_data["sworkPlacePhone"] = request.POST['sworkPlacePhone']

            insert_data["semail"] = form.cleaned_data['semail']

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

        membership_application.initialDate = datetime.strftime(membership_application.initialDate, '%d/%m/%Y')

        membership_application.finalDate = datetime.strftime(membership_application.finalDate, '%d/%m/%Y')

        ubigeo_service = UbigeoService()

        departments = ubigeo_service.distinctDepartment()

        filter_ubigeo = {}

        filter_ubigeo["department"] = membership_application.ubigeo.department

        provinces = ubigeo_service.distinctProvince(filter_ubigeo)

        filter_ubigeo = {}

        filter_ubigeo["province"] = membership_application.ubigeo.province

        districts = ubigeo_service.distinctDistrict(filter_ubigeo)

        context = {
            'types': types,
            'doc_types': doc_types,
            'departments': departments,
            'provinces': provinces,
            'districts': districts,
            'membership_application': membership_application,
        }

        return render(request2, 'Admin/Membership/edit_membership_request.html', context)


#USUARIO
@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['GET'])
def user_index(request):

    member_application_service = Membership_ApplicationService()

    identity_document_type_service = IdentityDocumentTypeService()

    member_service = MembersService()

    doc_types = identity_document_type_service.getIdentityDocumentTypes()

    membershipApplications = member_application_service.getMembership_Applications()

    objection_service = ObjectionsService()

    current_user = request.user

    member = member_service.getMemberByUser(current_user)

    filter_data = {}

    filter_data["member"] = member

    filter_data["status"] = 1

    for membership_application in membershipApplications:

        filter_data["membership_application"] = membership_application

        objections = objection_service.filter(filter_data)

        if len(objections) == 0:

            membership_application.objection = False

        else:

            membership_application.objection = True

    context = {
        'membershipApplications' : membershipApplications,
        'doc_types' : doc_types,
    }

    if request.session.has_key('objection_inserted'):

        context.update({'objection_inserted':request.session.get('objection_inserted')})

        del request.session['objection_inserted']

    elif request.session.has_key('objection_deleted'):

        context.update({'objection_deleted':request.session.get('objection_deleted')})

        del request.session['objection_deleted']

    return render(request, 'User/Membership/index_membership_request.html', context) 



#OBJECIONES
@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def create_objection(request):

    form = oforms.ObjectionForm(request.POST, request.FILES)

    requestId = request.POST['id_membership']

    memberId = request.POST['id_member']

    comments = request.POST['comments']

    current_user = request.user

    request2 = FormValidator.validateForm(form, request)

    objection_service = ObjectionsService()

    member_application_service = Membership_ApplicationService()

    member_service = MembersService()

    membership_application = member_application_service.getMembership_Application(requestId)

    member = member_service.getMemberByUser(current_user)
        
    filter_data = {}

    filter_data["member"] = member

    filter_data["membership_application"] = membership_application

    objections = objection_service.filter(filter_data)

    if len(objections) == 0:

        objection = ''

    else:

        objection = objections[0].comments

    if not request2:

        insert_data = {}

        insert_data["comments"] = comments

        insert_data["membership_application_id"] = requestId

        insert_data["member_id"] = memberId

        insert_data['date'] = datetime.now()

        insert_data["status"] = 1

        if objection == '':

            objection_service.create(insert_data)

        else:

            objection_service.update(objections[0].id, insert_data)

        request.session['objection_inserted'] = "True"

        return HttpResponseRedirect(reverse('membership_application:user_index'))

    else:
        

        context = {
            'membership_application': membership_application,
            'member' : member,
            'objection' : objection
        }

        return render(request, 'User/Membership/objections_members.html', context)


@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def objection_index(request):

    member_application_service = Membership_ApplicationService()

    requestId = request.POST['id']

    membership_application = member_application_service.getMembership_Application(requestId)

    member_service = MembersService()

    objection_service = ObjectionsService()

    current_user = request.user

    member = member_service.getMemberByUser(current_user)

    filter_data = {}

    filter_data["member"] = member

    filter_data["status"] = 1

    filter_data["membership_application"] = membership_application

    objections = objection_service.filter(filter_data)

    if len(objections) == 0:

        objection = ''

    else:

        objection = objections[0].comments

    context = {
        'membership_application' : membership_application,
        'member': member,
        'objection': objection
    }

    return render(request, 'User/Membership/objections_members.html', context)

@login_required
@permission_required('dummy.permission_usuario', login_url='login:ini')
@require_http_methods(['POST'])
def delete_objection(request):

    current_user = request.user

    member_application_service = Membership_ApplicationService()

    member_service = MembersService()

    objection_service = ObjectionsService()

    requestId = request.POST['id']

    membership_application = member_application_service.getMembership_Application(requestId)

    member = member_service.getMemberByUser(current_user)

    edit_data = {}

    filter_data = {}

    filter_data["member"] = member

    filter_data["membership_application"] = membership_application

    objections = objection_service.filter(filter_data)

    if len(objections) == 0:

        return HttpResponseRedirect(reverse('membership_application:user_index'))

    else:

        id = objections[0].id

        edit_data['status'] = 0

        objection_service.update(id, edit_data)

        request.session['objection_deleted'] = "True"

        return HttpResponseRedirect(reverse('membership_application:user_index'))


@login_required
@permission_required('dummy.permission_membresia', login_url='login:ini')
@require_http_methods(['POST'])
def approve_membership_application(request):

    if 'Accept' in request.POST:
    
        id_application = request.POST['id']

        member_application_service = Membership_ApplicationService()

        identity_doc_type_service = IdentityDocumentTypeService()

        doc_types = identity_doc_type_service.getIdentityDocumentTypes()

        membership_application =  member_application_service.getMembership_Application(id_application)

        ubigeo_service = UbigeoService()

        ubigeo = ubigeo_service.distinctDepartment()

        context = {
            'titulo' : 'titulo',
            'doc_types' : doc_types,
            'ubigeo' : ubigeo,
            'membership_application' : membership_application,
        }

        return render(request, 'Admin/Membership/new_membership_member.html', context)

    elif 'Reject' in request.POST:

        insert_data = {}

        id_application = request.POST['id']

        insert_data["status"] = 3

        member_application_service = Membership_ApplicationService()

        member_application_service.update(id_application, insert_data)

        return HttpResponseRedirect(reverse('membership_application:index'))



@login_required
@require_http_methods(['POST'])
def verify_document_number(request):

    if not isinstance(request.POST['name'], int):

        username = request.POST['name']

        if User.objects.filter(username=username).exists():

            return  HttpResponse("false")

        return  HttpResponse("true")


    member_application_service = Membership_ApplicationService()

    member_service = MembersService()

    affiliate_service = AffiliateService()

    filter_data = {}

    filter_data["document_number"] = request.POST['name']

    filter_data["status"] = 1

    filter_data2 = {}

    filter_data2["document_number"] = request.POST['name']

    filter_data2["state"] = 1

    if( member_service.filter(filter_data2)):

        return  HttpResponse("false")

    if( member_application_service.filter(filter_data)):

        return  HttpResponse("false")

    if( affiliate_service.filter(filter_data2)):

        return  HttpResponse("false")

    return  HttpResponse("true")
