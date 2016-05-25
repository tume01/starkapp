from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.BungalowsService import BungalowsService
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def index(request):

    servicio_service = ServiciosService()

    servicios = servicio_service.getServicios()

    context = {
        'servicios' : servicios,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Services/index_service.html', context) 


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Services/new_service.html', context)