from datetime import datetime
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.HeadquarterService import HeadquarterService
from services.UbigeoService import UbigeoService

from adapters.FormValidator import FormValidator
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import HeadquarterForm

# Create your views here.



@require_http_methods(['GET'])
def index(request):

    headquarter_service = HeadquarterService()
    
    headquarters = headquarter_service.filter({'status': 1})

    context = {
        'headquarters': headquarters,
        'titulo': 'tittle',
    }

    return render(request, 'Admin/Headquarters/index_headquarter.html', context)


@require_http_methods(['GET'])
def create_headquarters_index(request):
    headquarter_service = HeadquarterService()
    ubigeo_service = UbigeoService()

    headquarters = headquarter_service.getHeadquarters()
    ubigeos = ubigeo_service.distinctDepartment()

    context = {     
        'headquarters': headquarters,
        'ubigeos': ubigeos
    }
    
    return render(request, 'Admin/Headquarters/new_headquarter.html', context)


@require_http_methods(['POST'])
def create_headquarters(request):
    form = HeadquarterForm(request.POST)

    headquarter_service = HeadquarterService()
    ubigeo_service = UbigeoService()

    if not FormValidator.validateForm(form, request):
        
        insert_data = {}
        insert_data["name"] = form.cleaned_data['name']
        insert_data["location"] = form.cleaned_data['location']
        insert_data["description"] = form.cleaned_data['description']
        insert_data["status"] = 1

        filter_ubigeo = {}
        filter_ubigeo["department"] = request.POST['department']
        filter_ubigeo["province"] = request.POST['province']
        filter_ubigeo["district"] = request.POST['district']
        ubigeo = ubigeo_service.filter(filter_ubigeo)
        insert_data['ubigeos'] = ubigeo[0]
        
        headquarter_service.create(insert_data)
        
        return HttpResponseRedirect(reverse('headquarters:index'))
    else:

        headquarters = headquarter_service.getHeadquarters()
        ubigeos = ubigeo_service.distinctDepartment()

        context = {
            'headquarters': headquarters,
            'ubigeos': ubigeos
        }
        
        return render(request, 'Admin/Headquarters/new_headquarter.html', context)



@require_http_methods(['GET'])
def update_headquarters_index(request, headquarter_id):

    headquarter_service = HeadquarterService()
    ubigeo_service = UbigeoService()

    headquarter = headquarter_service.findHeadquarter(headquarter_id)
    ubigeos = ubigeo_service.getAllUbigeo()

    departments = ubigeo_service.distinctDepartment()
    filter_ubigeo = {}
    filter_ubigeo["department"] = headquarter.ubigeos.department

    provinces = ubigeo_service.distinctProvince(filter_ubigeo)
    filter_ubigeo = {}
    filter_ubigeo["province"] = headquarter.ubigeos.province

    districts = ubigeo_service.distinctDistrict(filter_ubigeo)

    context = {     
        'headquarter': headquarter,
        'ubigeos': ubigeos,
        'departments' : departments,
        'provinces' : provinces,
        'districts' : districts,
    }
    
    return render(request, 'Admin/Headquarters/edit_headquarter.html', context)



@require_http_methods(['POST']) 
def update_headquarters(request, headquarter_id):
    
    form = HeadquarterForm(request.POST)
    
    if FormValidator.validateForm(form, request):        
        return HttpResponseRedirect(reverse('headquarters:select', args=[headquarter_id]))

    else:
        
        headquarter_service = HeadquarterService()
        ubigeo_service = UbigeoService()

        edit_data = {}
        edit_data["name"] = form.cleaned_data['name']
        edit_data["location"] = form.cleaned_data['location']
        edit_data["description"] = form.cleaned_data['description']

        filter_ubigeo = {}
        filter_ubigeo["department"] = request.POST['department']
        filter_ubigeo["province"] = request.POST['province']
        filter_ubigeo["district"] = request.POST['district']
        ubigeo = ubigeo_service.filter(filter_ubigeo)
        edit_data["ubigeos"] = ubigeo[0]

        headquarter_service.update(headquarter_id, edit_data)

        return HttpResponseRedirect(reverse('headquarters:index'))


@require_http_methods(['GET'])
def delete(request, headquarter_id):

    headquarter_service = HeadquarterService()

    headquarter = headquarter_service.update(headquarter_id, {'status': 0})

    return HttpResponseRedirect(reverse('headquarters:index'))
