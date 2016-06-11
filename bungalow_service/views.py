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


@require_http_methods(['POST'])
def saveServicesByBungalowType(request, id):

    update_data = {}
    req = json.loads( request.body.decode('utf-8') )
    print(req.get("arrayIdServices"))

    bungalow_type = BungalowTypeService.findBungalowType(id)

    update_data["name"] = bungalow_type.name
    update_data["description"] = bungalow_type.description
    update_data["price"] = bungalow_type.price
    update_data["capacity"] = bungalow_type.capacity
    update_data["deleted_at"] = bungalow_type.deleted_at

    list_services = []
    for i in req.get("arrayIdServices"):
        list_services.append(Bungalow_serviceService.findBungalow_service(i))

    update_data["bungalow_services"] = list_services

    BungalowTypeService.update(id, update_data);


    return HttpResponse( json.dumps(req), content_type='application/json')

