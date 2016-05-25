from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.UserTypeService import UsersTypeService
from services.UsersService import UsersService
from django.views.decorators.http import require_http_methods
from Adapters.FormValidator import FormValidator
from .forms import UserForm, UserTypeForm


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

    form = UserTypeForm(request.POST)

    request = FormValidator.validateForm(form, request)

    if not request:

        insert_data = {}

        insert_data["description"] = form.cleaned_data['description']

        user_type_service = UsersTypeService()

        user_type_service.create(insert_data)

        return HttpResponseRedirect(reverse('users:type/index'))

    else:

        context = {
            'titulo' : 'titulo'
        }

        return render(request, 'Admin/Users/new_type_user.html', context)



@require_http_methods(['POST'])
def edit_user_type(request):

    form = UserTypeForm(request.POST)

    id_edit = request.POST['id']

    user_type_service = UsersTypeService()

    if FormValidator.validateForm(form, request):

        user_type = user_type_service.getType(id_edit)

        context = {
            'type' : user_type
        }

        return render(request, 'Admin/Users/edit_type_user.html', context)

    else:

        edit_data = {}

        edit_data["description"] = form.cleaned_data['description']

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

    form = UserForm(request.POST)

    id_edit = request.POST['id']

    user_service = UsersService()

    user_type_service = UsersTypeService()

    if FormValidator.validateForm(form, request):

        user = user_service.getUser(id_edit)

        types = user_type_service.getTypes()

        context = {
            'user' : user,
            'types' : types,
        }

        return render(request, 'Admin/Users/edit_user.html', context)

    else:

        edit_data = {}

        edit_data["name"] = form.cleaned_data['name']

        edit_data["password"] = form.cleaned_data['password']

        user_type = user_type_service.getType(form.cleaned_data['user_type'])

        edit_data["user_type"] = user_type

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

    form = UserForm(request.POST)

    request = FormValidator.validateForm(form, request)

    user_type_service = UsersTypeService()

    if not request:

        insert_data = {}

        insert_data["name"] = form.cleaned_data['name']

        insert_data["password"] = form.cleaned_data['password']

        user_type = user_type_service.getType(form.cleaned_data['user_type'])

        insert_data["user_type"] = user_type

        user_service = UsersService()

        user_service.create(insert_data)

        return HttpResponseRedirect(reverse('users:index'))

    else:

        types = user_type_service.getTypes()

        context = {
            'titulo' : 'titulo',
            'types' : types
        }

        return render(request, 'Admin/Users/new_user.html', context)



@require_http_methods(['GET'])
def user_index(request):

    user_service = UsersService()

    users = user_service.getUsers()

    #user_type_service = UsersTypeService()

    #for user in users:
        #user.user_type = user_type_service.getType(user.user_type_id).description

    context = {
        'users' : users,
    }

    return render(request, 'Admin/Users/index_user.html', context) 
