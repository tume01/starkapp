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

    environments = environment_service.getEnvironment()

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

@require_http_methods(['POST'])
def create_bungalow(request):

    insert_data = {}

    insert_data["number"] = request.POST['number']

    insert_data["location"] = request.POST['location']

    insert_data["status"] = request.POST['status']

    insert_data["bungalow_type_id"] = 1

    bungalow_service = EnvironmentService()

    bungalow_service.create(insert_data)

    return HttpResponseRedirect(reverse('environment:index'))
