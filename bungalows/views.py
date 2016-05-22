from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.BungalowsService import BungalowsService
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def index(request):

    bungalow_service = BungalowsService()

    bungalows = bungalow_service.getBungalows()

    context = {
        'bungalows' : bungalows,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Bungalows/index_bungalow.html', context) 

@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Bungalows/new_bungalow.html', context)

@require_http_methods(['POST'])
def create_bungalow(request):

    insert_data = {}

    insert_data["number"] = request.POST['number']

    insert_data["location"] = request.POST['location']

    insert_data["status"] = request.POST['status']

    insert_data["bungalow_type_id"] = 1

    bungalow_service = BungalowsService()

    bungalow_service.create(insert_data)

    return HttpResponseRedirect(reverse('bungalows:index'))
