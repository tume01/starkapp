from .forms import UpdateServicioForm
from .forms import ServicioForm
from adapters.FormValidator import FormValidator

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

    form = ServicioForm(request.POST)

    context = {
        'titulo': 'titulo'
    }

    request = FormValidator.validateForm(form, request)

    servicio_service = ServiciosService()

    if not request:

        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        servicio_type_id = form.cleaned_data['id_servicio']

        insert_data = {
            'name': name,
            'price': price,
            'servicio_type_id': servicio_type_id
        }

        servicio_service.create(insert_data)

        return HttpResponseRedirect(reverse('servicios:index'))

    else:
        servicio_types = servicio_service.getServicioTypes()
        context = {
            'servicio_types' : servicio_types
        }

        return render(request, 'Admin/Services/new_service.html', context)

@require_http_methods(['GET'])
def update_index(request, servicio_id):

    servicio_service = ServiciosService()

    servicio = servicio_service.findServicio(servicio_id)

    context = {
        'titulo' : 'titulo',
        'servicio' : servicio
    }

    return render(request, 'Admin/Services/edit_service.html', context)

@require_http_methods(['POST'])
def update_servicio(request, servicio_id):

    form = UpdateServicioForm(request.POST)

    servicio_service = ServiciosService()

    servicio = servicio_service.findServicio(servicio_id)

    if FormValidator.validateForm(form, request):
        context = {
            'titulo': 'titulo',
            'servicio' : servicio
        }
        return render(request, 'Admin/Services/edit_service.html', context)

    else:
        
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']


        update_data = {
            'price': price,
            'name' : name
        }

        servicio_service.update(servicio_id, update_data)

        return HttpResponseRedirect(reverse('servicios:index'))

@require_http_methods(['GET'])
def delete(request, servicio_id):
    
    servicio_service = ServiciosService()

    servicio = servicio_service.delete(servicio_id)

    return HttpResponseRedirect(reverse('servicios:index'))