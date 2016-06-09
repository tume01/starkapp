from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from services.BungalowTypeService import BungalowTypeService
from services.Bungalow_serviceService import Bungalow_serviceService

import json
import urllib
import logging
from django.db import IntegrityError, transaction

# Create your views here.

@require_http_methods(['GET'])
def index(request):

    context = {
        'bungalowTypes': BungalowTypeService.getBungalowTypes(),
        'bungalow_services': Bungalow_serviceService.getBungalow_services(),
        'titulo': 'titulo'
    }

    return render(request, 'Admin/bungalow_service/index.html', context)


@require_http_methods(['POST'])
def getServices(request, id):
    req_list= []

    if int(id) >= 0:
        bungalow_type = BungalowTypeService.findBungalowType(id)

        for s in bungalow_type.bungalow_services.all():
        	service_data = {}
        	service_data["id"] = s.id
        	service_data["text"] = s.name
        	req_list.append(service_data)
        	print(s.id)


    return HttpResponse( json.dumps(req_list), content_type='application/json')

