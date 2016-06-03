from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.FineTypeService import FineTypeService
from services.MemberService import MembersService
from services.FineService import FineService
from django.views.decorators.http import require_http_methods
from Adapters.FormValidator import FormValidator
from .forms import FineForm
from .forms import FineTypeForm

@require_http_methods(['GET'])
def type_index(request):

    fine_type_service = FineTypeService()

    fines = fine_type_service.getFines()

    context = {
        'fines' : fines,
    }

    return render(request, 'Admin/Fines/index_type_fine.html', context) 


@require_http_methods(['GET'])
def create_type_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Fines/new_type_fine.html', context)

@require_http_methods(['POST'])
def edit_type_index(request):

    id_fine = request.POST['id']

    fine_type_service = FineTypeService()

    fine = fine_type_service.getFine(id_fine)

    context = {
        'fine' : fine,
    }

    return render(request, 'Admin/Fines/edit_type_fine.html', context)

@require_http_methods(['POST'])
def delete_type(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    filter_data = {}

    filter_data["fine_type_id"] = id_edit

    filter_data["status"] = 'Pendiente de Pago'

    fine_service = FineService()

    fines = fine_service.filter(filter_data)

    if(len(fines) == 0):

        fine_type_service = FineTypeService()

        fine_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('fine:index_type'))


@require_http_methods(['POST'])
def create_type(request):

    form = FineTypeForm(request.POST)

    request = FormValidator.validateForm(form, request)

    if not request:

        insert_data = {}

        insert_data["reason"] = form.cleaned_data['reason']

        insert_data["price"] = form.cleaned_data['price']

        insert_data["status"] = 1

        fine_type_service = FineTypeService()

        fine_type_service.create(insert_data)

        return HttpResponseRedirect(reverse('fine:index_type'))

    else:
        context = {
            'titulo': 'titulo'
        }

        return render(request, 'Admin/Fines/new_type_fine.html', context)




@require_http_methods(['POST'])
def edit_type(request):

    form = FineTypeForm(request.POST)

    id_edit = request.POST['id']

    if FormValidator.validateForm(form, request):

        fine_type_service = FineTypeService()

        fine = fine_type_service.getFine(id_edit)

        context = {
            'fine': fine,
        }

        return render(request, 'Admin/Fines/edit_type_fine.html', context)

    else:

        edit_data = {}

        edit_data["reason"] = form.cleaned_data['reason']

        edit_data["price"] = form.cleaned_data['price']

        fine_type_service = FineTypeService()

        fine_type_service.update(id_edit, edit_data)

        return HttpResponseRedirect(reverse('fine:index_type'))


@require_http_methods(['POST'])
def create_index(request):

    member_id = request.POST['id']

    fine_type_service = FineTypeService()

    types = fine_type_service.getFines()

    context = {
        'member_id' : member_id,
        'types' : types,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Fines/new_fine.html', context)

@require_http_methods(['POST'])
def create(request2):

    form = FineForm(request2.POST)

    request = FormValidator.validateForm(form, request2)

    member_id = request2.POST['member_id']

    if not request:

        insert_data = {}

        insert_data["status"] = 'Pendiente de Pago'

        insert_data["observations"] = form.cleaned_data['observations']

        insert_data["member_id"] = request2.POST['member_id']

        insert_data["fine_type_id"] = request2.POST['fine_type_id_id']

        insert_data["member_id"] = member_id

        fine_service = FineService()

        fine_service.create(insert_data)

        return HttpResponseRedirect(reverse('members:index'))

    else:

        fine_type_service = FineTypeService()

        types = fine_type_service.getFines()

        context = {
            'member_id': member_id,
            'types': types,
            'titulo': 'titulo'
        }

        return render(request, 'Admin/Fines/new_fine.html', context)

@require_http_methods(['POST'])
def index(request):

    member_id = request.POST['id']

    member_service = MembersService()

    member = member_service.getMember(member_id)

    fine_service = FineService()

    fine_type_service = FineTypeService()

    fines = fine_service.getFineByUser(member_id)

    for fine in fines:
        fine.reason = (fine_type_service.getFine(fine.fine_type.id)).reason
        fine.price = (fine_type_service.getFine(fine.fine_type.id)).price

    context = {
        'fines' : fines,
        'member' : member,
    }

    return render(request, 'Admin/Fines/index_fine.html', context)


@require_http_methods(['POST'])
def filter(request):

    member_id = request.POST['member_id']

    member_service = MembersService()

    member = member_service.getMember(member_id)

    fine_service = FineService()

    fine_type_service = FineTypeService()

    filter_fines = {}

    fineStatus = request.POST['status']

    filter_fines["member_id"] = member_id

    if fineStatus != 'Pendiente de Pago':
        filter_fines["status"] = fineStatus

    fines = fine_service.filter(filter_fines)

    for fine in fines:
        fine.reason = (fine_type_service.getFine(fine.fine_type.id)).reason
        fine.price = (fine_type_service.getFine(fine.fine_type.id)).price

    context = {
        'fines': fines,
        'member' : member,
    }

    return render(request, 'Admin/Fines/index_fine.html', context)