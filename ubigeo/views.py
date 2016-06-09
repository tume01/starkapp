from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.UbigeoService import UbigeoService
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
@login_required
@require_http_methods(['POST'])
def get_distritos(request):

    ubigeo_service = UbigeoService()

    filter_ubigeo = {}

    filter_ubigeo["province"] = request.POST['province']

    districts = ubigeo_service.distinctDistrict(filter_ubigeo)

    return  HttpResponse(json.dumps(list(districts)), content_type = "application/json")



@login_required
@require_http_methods(['POST'])
def get_provincias(request):

    ubigeo_service = UbigeoService()

    filter_ubigeo = {}

    filter_ubigeo["department"] = request.POST['department']

    provinces = ubigeo_service.distinctProvince(filter_ubigeo)

    return  HttpResponse(json.dumps(list(provinces)), content_type = "application/json")
