from django.shortcuts import render
from django.http import HttpResponse
from services.BungalowsService import BungalowsService
# Create your views here.

def index(request):

    x = BungalowsService()

    y = x.test()

    return HttpResponse(y)