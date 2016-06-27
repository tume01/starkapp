from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.ProvidersService import ProvidersService
from django.views.decorators.http import require_http_methods
from .forms import ProviderForm

from datetime import datetime,timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from services.ProviderTypeService import ProviderTypesService


@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
@require_http_methods(['GET'])
def index(request):

    provider_service = ProvidersService()

    filters = getProviderFilters(request)
    filters['provider_type_id'] = "1"

    providers2 = provider_service.filter(filters)

    providers = provider_service.getProviders()

    #p_type = 1

    context = {
        'proveedores' : providers2,
        'p_type' : 1,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Providers/index_provider.html', context)


@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
@require_http_methods(['GET'])
def index_concesionary(request):
    provider_service = ProvidersService()

    filters = getProviderFilters(request)

    providers2 = provider_service.filter(filters)

    providers = provider_service.getProviders()
    
    p_type = 1

    print("hbsakckcdcncnmcnmcnmxnmxnxnxnnx")
    print(p_type)

    context = {
        'proveedores' : providers2,
        'p_type' : 2,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Providers/index_provider.html', context)


@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
def getProviderFilters(request):

    filters = {}

    if request.GET.get('filter-ruc'):
        filters['ruc__contains'] = request.GET.get('filter-ruc')

    if request.GET.get('filter-status'):
        filters['status'] = request.GET.get('filter-status') 

    if request.GET.get('filter-registrationDate1'):
        start_date = datetime.strptime(request.GET.get('filter-registrationDate1'), "%d/%m/%Y")

        filters['registrationDate__gte'] = start_date

    if request.GET.get('filter-registrationDate2'):
        end_date = datetime.strptime(request.GET.get('filter-registrationDate2'), "%d/%m/%Y")
        #end_date = end_date + timedelta(hours=24)

        filters['registrationDate__lt'] = end_date

    if request.GET.get('filter-businessName'):
        filters['businessName'] = request.GET.get('filter-businessName')

    if request.GET.get('filter-contactName'):
        filters['contactName'] = request.GET.get('filter-contactName')

    return filters

@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
@require_http_methods(['GET'])
def create_index(request):

    #regions = Region.objects.all()
    form = ProviderForm()
    #form.region = regions
    context = {
        'titulo' : 'titulo',
        'p_type' : 1,
        'form' : form
    }

    return render(request, 'Admin/Providers/new_provider.html', context)


@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
@require_http_methods(['GET'])
def create_index_concesionary(request):

    #regions = Region.objects.all()
    form = ProviderForm()
    #form.region = regions
    context = {
        'titulo' : 'titulo',
        'p_type' : 2,
        'form' : form
    }

    return render(request, 'Admin/Providers/new_provider.html', context)

@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
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

                insert_data["provider_type"] = ProviderTypesService().find(1)
                insert_data["vigencyDate"] = datetime.now()+timedelta(days=30)

                provider_service = ProvidersService()

                provider_service.create(insert_data)

                return HttpResponseRedirect(reverse('providers:index'))
            else:
                context = {'form' : form, 'p_type' : 1}
                return render(request, 'Admin/Providers/new_provider.html', context)
        else:
            #form = ProviderForm()
            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form, 'p_type' : 1}
            return render(request, 'Admin/Providers/new_provider.html', context)


@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
@require_http_methods(['POST'])
def create_concesionary(request):

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

                insert_data["provider_type"] = ProviderTypesService().find(2)
                insert_data["vigencyDate"] = datetime.now()+timedelta(days=30)

                provider_service = ProvidersService()

                provider_service.create(insert_data)

                return HttpResponseRedirect(reverse('providers:index_concesionary'))
            else:
                context = {'form' : form, 'p_type' : 2}
                return render(request, 'Admin/Providers/new_provider.html', context)
        else:
            #form = ProviderForm()
            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form, 'p_type' : 2}
            return render(request, 'Admin/Providers/new_provider.html', context)





@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
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
        'p_type' : 1,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Providers/edit_provider.html', context)


@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
@require_http_methods(['GET'])
def edit_index_concesionary(request,id):

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
        'p_type' : 2,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Providers/edit_provider.html', context)


@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
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

@login_required
@permission_required('dummy.permission_proveedor', login_url='login:iniAdmin')
@require_http_methods(['POST'])
def filter_product(request):
    filter_data = {}
    req = json.loads( request.body.decode('utf-8') )

    print("id= "+req.get("id"))


    product_name = ""

    qry = "SELECT p.id, p.businessName, p.status, p.registrationDate, p.contactName, p.contactPhone, p.email "
    qry += " FROM providers_provider p "


    if req.get("f_ruc") == '' and req.get("f_businessName") == '' and req.get("f_registrationDate1") == '' and req.get("f_registrationDate2") == '' and req.get("f_contactName") == '':
        print("sin filtro")
    else:
        if req.get("f_selectProductType") != '0':
            qry += " AND p.product_type_id="+req.get("f_selectProductType") + " "
        
        if req.get("f_select2Provider") != None:
            i=0
            for prov_id in req.get("f_select2Provider"):
                if i == 0:
                    qry += " AND ( pxp.provider_id="+ prov_id + " "
                    i += 1
                else:
                    qry += " OR pxp.provider_id="+ prov_id + " "

            qry += " ) "

        if req.get("f_name") != '':
            qry += " AND p.name LIKE %s"
            product_name = req.get("f_name")

    print("qry= "+qry)

    req_list = []

    try:
        if product_name != '':
            list_products = Product.objects.raw(qry, [product_name])
        else:
            list_products = Product.objects.raw(qry)
        
        for p in list_products:
            data_item = {}
            data_item["id"] = p.id
            data_item["name"] = p.name
            data_item["price"] = p.price
            data_item["actual_stock"] = p.actual_stock
            data_item["minimum_stock"] = p.minimum_stock
            data_item["status"] = p.status
            data_item["description"] = p.description
            #data_item["id"] = p.id
            req_list.append(data_item)

    except IntegrityError:
        handle_exception()
        list_products = None

    return HttpResponse( json.dumps(req_list), content_type='application/json')