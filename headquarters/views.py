from datetime import datetime
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.HeadquarterService import HeadquarterService

from Adapters.FormValidator import FormValidator
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import HeadquarterForm

# Create your views here.



@require_http_methods(['GET'])
def index(request):

    headquarter_service = HeadquarterService()
    
    headquarters = headquarter_service.filter({'status': None})

    context = {
        'headquarters': headquarters,
        'titulo': 'tittle',
    }

    return render(request, 'Admin/Headquarters/index_headquarter.html', context)



@require_http_methods(['GET'])
def create_headquarters_index(request):
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()

    context = {     
        'headquarters': headquarters
    }
    
    return render(request, 'Admin/Headquarters/new_headquarter.html', context)




@require_http_methods(['GET'])
def update_headquarters_index(request, headquarter_id):

    headquarter_service = HeadquarterService()

    headquarter = headquarter_service.findHeadquarter(headquarter_id)

    context = {     
        'headquarter': headquarter
    }
    
    return render(request, 'Admin/Headquarters/edit_headquarter.html', context)

@require_http_methods(['POST'])
def create_headquarters(request):

    form = HeadquarterForm(request.POST)

    headquarter_service = HeadquarterService()

    if not FormValidator.validateForm(form, request):
        
        insert_data = {}

        insert_data["name"] = form.cleaned_data['name']

        insert_data["location"] = form.cleaned_data['location']

        insert_data["description"] = form.cleaned_data['description']

        headquarter_service.create(insert_data)
        
        return HttpResponseRedirect(reverse('headquarters:index'))
    else:

        headquarters = headquarter_service.getHeadquarters()

        context = {     
            'headquarters': headquarters,
        }
        
        return render(request, 'Admin/Headquarters/new_headquarter.html', context)

@require_http_methods(['POST']) 
def update_headquarters(request, headquarter_id):
    
    form = HeadquarterForm(request.POST)
    
    if FormValidator.validateForm(form, request):
        
        return HttpResponseRedirect(reverse('headquarters:select', args=[headquarter_id]))

    else:
        
        headquarter_service = HeadquarterService()

        edit_data = {}

        edit_data["name"] = form.cleaned_data['name']

        edit_data["location"] = form.cleaned_data['location']       

        edit_data["description"] = form.cleaned_data['description']

        headquarter_service.update(headquarter_id, edit_data)

        return HttpResponseRedirect(reverse('headquarters:index'))

@require_http_methods(['GET'])
def delete(request, headquarter_id):

    headquarter_service = HeadquarterService()

    headquarter = headquarter_service.update(headquarter_id, {'status': datetime.now()})

    return HttpResponseRedirect(reverse('headquarters:index'))
