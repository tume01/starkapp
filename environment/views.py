from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.EnvironmentService import EnvironmentService
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def index(request):

    environment_service = EnvironmentService()

    environments = environment_service.getEnvironmentByStatus()

    context = {
        'environments' : environments,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/List_Environment.html', context)


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/Create_Environment.html', context)

@require_http_methods(['GET'])
def edit_index(request, id):

    environment_service = EnvironmentService()

    environments = environment_service.getEnviromentById(id)

    context = {
		'id' :id,
        'titulo': 'tittle',
        'environment' : environments,
    }

    return render(request, 'Admin/Environments/Edit_Environment.html', context)

@require_http_methods(['POST'])
def delete_environment(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    environment_service = EnvironmentService()

    environment_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('environment:index'))


@require_http_methods(['POST'])
def create_environment(request):

    insert_data = {}

    insert_data["name"] = request.POST['name']

    #insert_data["sede"] = request.POST['sede']

    insert_data["description"] = request.POST['description']

    insert_data["status"] = 1

    insert_data["capacity"] = request.POST['capacity']

    #insert_data["environment_id"] = request.POST['number']

    environment_service = EnvironmentService()

    environment_service.create(insert_data)

    return HttpResponseRedirect(reverse('environment:index'))


@require_http_methods(['POST'])
def edit_environment(request, id):

    edit_data = {}

    edit_data["description"] = request.POST['description']

    edit_data["name"] = request.POST['name']

    edit_data["capacity"] = request.POST['capacity']

    edit_data["status"] = request.POST['status']    

    environment_service = EnvironmentService()

    environment_service.update(id, edit_data)

    return HttpResponseRedirect(reverse('environment:index'))
