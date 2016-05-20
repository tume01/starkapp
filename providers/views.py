from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.ProvidersService import ProvidersService
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def index(request):

    provider_service = ProvidersService()

    providers = provider_service.getProviders()

    context = {
        'proveedores' : providers,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Providers/index_provider.html', context) 

@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Providers/new_provider.html', context)

@require_http_methods(['POST'])
def create_provider(request):

    insert_data = {}

    insert_data["idProvider"] = request.POST['idProvider']
    insert_data["ruc"] = request.POST['ruc']
    insert_data["businessName"] = request.POST['businessName']
    insert_data["status"] = request.POST['status']
    insert_data["distric"] = equest.POST['distric']    
    insert_data["province"] = equest.POST['province']
    insert_data["address"] = equest.POST['address']
    insert_data["phone"] = equest.POST['phone'] 
    insert_data["email"] = equest.POST['email']
    insert_data["registrationDate"] = equest.POST['registrationDate']
    insert_data["contactName"] = equest.POST['contactName'] 
    insert_data["contactPhone"] = equest.POST['contactPhone']
    insert_data["effectiveTime"] = equest.POST['effectiveTime']    

    provider_service = ProvidersService()

    provider_service.create(insert_data)

    return HttpResponseRedirect(reverse('providers:index'))
