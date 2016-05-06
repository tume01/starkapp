from django.shortcuts import render
from django.http import HttpResponse
from services.BungalowsService import BungalowsService

def index(request):

    bungalow_service = BungalowsService()

    bungalows = bungalow_service.getBungalows()

    return HttpResponse(bungalows)