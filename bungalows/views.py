from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from services.BungalowsService import BungalowsService

def index(request):

    template = loader.get_template('Index_bungalows_a.html')

    bungalow_service = BungalowsService()

    bungalows = bungalow_service.getBungalows()

    context = {
        'bungalows' : bungalows,
        "titulo" : 'titulo'
    }

    return HttpResponse(template.render(context, request))

def create_index(request):

    template = loader.get_template('New_bungalows.html')

    context = {
        "titulo" : 'titulo'
    }

    return HttpResponse(template.render(context, request))

def insert(request):

    insert_data = {}

    insert_data["number"] = request.POST['number']

    insert_data["location"] = request.POST['location']

    insert_data["status"] = request.POST['status']

    insert_data["bungalow_type_id_id"] = 1

    bungalow_service = BungalowsService()

    bungalow_service.create(insert_data)

    template = loader.get_template('Index_bungalows_a.html')

    bungalows = bungalow_service.getBungalows()

    context = {
        'bungalows' : bungalows,
        "titulo" : 'titulo'
    }

    return HttpResponse(template.render(context, request))     