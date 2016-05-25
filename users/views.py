from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.UserTypeService import UsersTypeService
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def user_type_index(request):

    user_type_service = UsersTypeService()

    types = user_type_service.getTypes()

    context = {
        'types' : types,
    }

    return render(request, 'Admin/Users/index_type_user.html', context) 


@require_http_methods(['GET'])
def create_user_type_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Users/new_type_user.html', context)

@require_http_methods(['POST'])
def edit_user_type_index(request):

    id_type = request.POST['id']

    user_type_service = UsersTypeService()

    type = user_type_service.getType(id_type)

    context = {
        'type' : type,
    }

    return render(request, 'Admin/Users/edit_type_user.html', context)


@require_http_methods(['POST'])
def create_user_type(request):

    insert_data = {}

    insert_data["description"] = request.POST['description']

    user_type_service = UsersTypeService()

    user_type_service.create(insert_data)

    return HttpResponseRedirect(reverse('users:type/index'))


@require_http_methods(['POST'])
def edit_user_type(request):

    edit_data = {}

    edit_data["description"] = request.POST['description']

    id_edit = request.POST['id']

    user_type_service = UsersTypeService()

    user_type_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('users:type/index'))
