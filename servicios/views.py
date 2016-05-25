from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.ServiciosService import ServiciosService
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

    servicio_service = ServiciosService()

    servicio_types = servicio_service.getServicioTypes()

    context = {
        'titulo' : 'titulo',
        'servicio_types' : servicio_types
    }

    return render(request, 'Admin/Services/new_service.html', context)

@require_http_methods(['POST'])
def create_servicio(request):

    insert_data = {}

    insert_data["name"] = request.POST['name']

    insert_data["price"] = request.POST['price']

    insert_data["servicio_type_id"] = request.POST['id_servicio']

    servicio_service = ServiciosService()

    servicio_service.create(insert_data)

    return HttpResponseRedirect(reverse('servicios:index'))