from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.ProvidersService import ProvidersService
from django.views.decorators.http import require_http_methods
from .forms import ProviderForm

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

    regions = Region.objects.all()
    form = ProviderForm()
    #form.region = regions
    context = {
        'titulo' : 'titulo',
        'form' : form
    }

    return render(request, 'Admin/Providers/new_provider.html', context)

@require_http_methods(['POST'])
def create_provider(request):

    if request.POST:
        form = ProviderForm(request.POST)
        
        #print(form['ruc'])
        if form.is_valid():
            print("no pasa")

            provider_service = ProvidersService()

            providerRuc = provider_service.find_ruc(request.POST['ruc'])

            if(providerRuc == None):
                print("pasa")
                insert_data = {}
                insert_data["ruc"] = request.POST['ruc']
                insert_data["businessName"] = request.POST['businessName']
                insert_data["status"] = request.POST['status']
                insert_data["distric"] = request.POST['distric']
                insert_data["province"] = request.POST['province']
                insert_data["region"] = request.POST['region']
                insert_data["address"] = request.POST['address']
                insert_data["postal"] = request.POST['postal']
                insert_data["phone"] = request.POST['phone']
                insert_data["email"] = request.POST['email']
                insert_data["registrationDate"] = request.POST['registrationDate']
                insert_data["contactName"] = request.POST['contactName']
                insert_data["contactPhone"] = request.POST['contactPhone']


                provider_service = ProvidersService()

                provider_service.create(insert_data)

                return HttpResponseRedirect(reverse('providers:index'))
            else:
                context = {'form' : form}
                return render(request, 'Admin/Providers/new_provider.html', context)
        else:
            #form = ProviderForm()
            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form}
            return render(request, 'Admin/Providers/new_provider.html', context)


@require_http_methods(['GET'])
def edit_index(request,id):

    provider_service = ProvidersService()

    provider = provider_service.find(id)
    print(id)
    #Falta validación de try except dentro de base repository
    if (provider == None):
        return HttpResponseRedirect(reverse('providers:index'))

    form = ProviderForm(instance=provider)

    context = {
        'id' : id,
        'form' : form,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Providers/edit_provider.html', context)

@require_http_methods(['POST'])
def edit_provider(request,id):


    if request.POST:
        form = ProviderForm(request.POST)
        
        #print(form['ruc'])
        if form.is_valid():

            #form.save()

            insert_data = {}
            insert_data["ruc"] = request.POST['ruc']
            insert_data["businessName"] = request.POST['businessName']
            insert_data["status"] = request.POST['status']
            insert_data["distric"] = request.POST['distric']
            insert_data["province"] = request.POST['province']
            insert_data["region"] = request.POST['region']
            insert_data["address"] = request.POST['address']
            insert_data["postal"] = request.POST['postal']
            insert_data["phone"] = request.POST['phone']
            insert_data["email"] = request.POST['email']
            insert_data["registrationDate"] = request.POST['registrationDate']
            insert_data["contactName"] = request.POST['contactName']
            insert_data["contactPhone"] = request.POST['contactPhone']



            provider_service = ProvidersService()

            provider_service.update(id,insert_data)

            return HttpResponseRedirect(reverse('providers:index'))
        else:
            #form = ProviderForm()
            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form}
            return render(request, 'Admin/Providers/edit_provider.html', context)