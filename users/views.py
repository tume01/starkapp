from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.UserTypeService import UsersTypeService
from services.UsersService import UsersService
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



@require_http_methods(['POST'])
def edit_user_index(request):

    id_user = request.POST['id']

    user_service = UsersService()

    user = user_service.getUser(id_user)

    user_type_service = UsersTypeService()

    types = user_type_service.getTypes()

    context = {
        'user' : user,
        'types' : types,
    }

    return render(request, 'Admin/Users/edit_user.html', context)

@require_http_methods(['POST'])
def edit_user(request):

    edit_data = {}

    edit_data["name"] = request.POST['name']

    edit_data["password"] = request.POST['password']

    edit_data["user_type_id"] = request.POST['user_type_id']

    id_edit = request.POST['id']

    user_service = UsersService()

    user_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('users:index'))


@require_http_methods(['GET'])
def create_user_index(request):

    user_type_service = UsersTypeService()

    types = user_type_service.getTypes()

    context = {
        'titulo' : 'titulo',
        'types' : types,
    }

    return render(request, 'Admin/Users/new_user.html', context)


@require_http_methods(['POST'])
def create_user(request):

    insert_data = {}

    insert_data["name"] = request.POST['name']

    insert_data["password"] = request.POST['password']

    insert_data["user_type_id"] = request.POST['user_type_id']

    user_service = UsersService()

    user_service.create(insert_data)

    return HttpResponseRedirect(reverse('members:index'))


@require_http_methods(['GET'])
def user_index(request):

    user_service = UsersService()

    users = user_service.getUsers()

    user_type_service = UsersTypeService()

    for user in users:
        user.user_type_id = user_type_service.getType(user.user_type_id).description

    context = {
        'users' : users,
    }

    return render(request, 'Admin/Users/index_user.html', context) 