from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.FineTypeService import FineTypeService
from services.FineService import FineService
from django.views.decorators.http import require_http_methods


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

    fine_type_service = FineTypeService()

    fine_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('fine:index_type'))


@require_http_methods(['POST'])
def create_type(request):

    insert_data = {}

    insert_data["reason"] = request.POST['reason']

    insert_data["price"] = request.POST['price']

    insert_data["status"] = 1

    fine_type_service = FineTypeService()

    fine_type_service.create(insert_data)

    return HttpResponseRedirect(reverse('fine:index_type'))


@require_http_methods(['POST'])
def edit_type(request):

    edit_data = {}

    edit_data["reason"] = request.POST['reason']

    edit_data["price"] = request.POST['price']

    id_edit = request.POST['id']

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
def create(request):

    insert_data = {}

    insert_data["status"] = 1

    insert_data["observations"] = request.POST['observations']

    insert_data["fine_type_id_id"] = request.POST['fine_type_id_id']

    insert_data["member_id"] = request.POST['member_id']

    fine_service = FineService()

    fine_service.create(insert_data)

    return HttpResponseRedirect(reverse('members:index'))