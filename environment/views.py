from datetime import datetime
import json
from .forms import EnvReservationForm
from adapters.FormValidator import FormValidator
from django.contrib import messages
from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.EnvironmentService import EnvironmentService
from services.EnvironmentTypeService import EnvironmentTypeService
from services.HeadquarterService import HeadquarterService
from django.views.decorators.http import require_http_methods
from .forms import EnvironmentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@require_http_methods(['GET'])
def index(request):

    environment_service = EnvironmentService()
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()
    environments = environment_service.getEnvironmentByStatus()

    context = {
        'environments' : environments,
        'headquarters' : headquarters,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/List_Environment.html', context)

@require_http_methods(['GET'])
def create_index(request):

    form = EnvironmentForm()

    environment_service = EnvironmentTypeService()
    type_environment = environment_service.getEnvironment()
    headquarter_service = HeadquarterService()
    headquarters = headquarter_service.getHeadquarters()

    context = {
        'titulo' : 'titulo',
        'type_environment' : type_environment,
        'headquarters' : headquarters,
        'form' : form
    }

    return render(request, 'Admin/Environments/Create_Environment.html', context)

@require_http_methods(['GET'])
def edit_index(request, id):

    environment_service = EnvironmentService()
    environment_type_service = EnvironmentTypeService()
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()
    environments = environment_service.getEnviromentById(id)
    type_environment = environment_type_service.getEnvironment()

    print(id)
    #Falta validación de try except dentro de base repository
    if (environments == None):
        return HttpResponseRedirect(reverse('Environments:index'))

    form = EnvironmentForm(instance=environments)
    context = {
		'id' :id,
        'form' : form,
        'environments' : environments,
        'type_environment' : type_environment,
        'headquarters': headquarters,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/Edit_Environment.html', context)

@require_http_methods(['POST'])
def delete_environment(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    environment_service = EnvironmentService()

    environment_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('environment:index'))


@require_http_methods(['POST'])
def create_environment(request):
    if request.POST:
        form = EnvironmentForm(request.POST)
        
        if form.is_valid():
            print("pasa")
            insert_data = {}
            insert_data["name"] = request.POST['name']
            insert_data["capacity"] = request.POST['capacity']
            insert_data["status"] = request.POST['status']
            insert_data["environment_type_id"] = request.POST['environment_type']
            insert_data["headquarter_id"] = request.POST['headquarter']
            insert_data["description"] = request.POST['description']
                
            environment_service = EnvironmentService()

            environment_service.create(insert_data)

            return HttpResponseRedirect(reverse('environment:index'))

        else:

            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form}
            return render(request, 'Admin/Environments/Create_Environment.html', context)


@require_http_methods(['POST'])
def edit_environment(request, id):
    if request.POST:
        form = EnvironmentForm(request.POST)
        
        if form.is_valid():

            #form.save()

            edit_data = {}
            edit_data["name"] = request.POST['name']
            edit_data["capacity"] = request.POST['capacity']
            edit_data["status"] = request.POST['status']
            edit_data["environment_type_id"] = request.POST['environment_type']
            edit_data["headquarter_id"] = request.POST['headquarter']
            edit_data["description"] = request.POST['description']

            environment_service = EnvironmentService()

            environment_service.update(id, edit_data)

            return HttpResponseRedirect(reverse('environment:index'))
        else:

            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form}
            return render(request, 'Admin/Environments/Edit_Environment.html', context)

    return HttpResponseRedirect(reverse('environment:index'))


# Metodos para la reserva de ambientes

@require_http_methods(['GET'])
def index_book(request):

    environment_service = EnvironmentService()
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()

    filters      = getReservationFilters(request)
    reservations = environment_service.filterReservations(filters)

    paginator = Paginator(reservations, 10)

    page = request.GET.get('page')

    try:
        reservations = paginator.page(page)

    except PageNotAnInteger:
        reservations = paginator.page(1)

    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)

    context = {
        'reservations' : reservations,
        'headquarters' : headquarters,
        'titulo'       : 'titulo'
    }

    return render(request, 'Admin/Environments/List_Reservations.html', context)


def getReservationFilters(request):


    filters = {}

    if request.GET.get('env_name') or request.GET.get('headquarter_id') or request.GET.get('environment_id'):

        environment_service = EnvironmentService()
        data = {}

        if request.GET.get('env_name'):
            data['name__icontains'] = request.GET.get('env_name')

        if request.GET.get('headquarter_id'):
            data['headquarter_id'] = request.GET.get('headquarter_id')

        if request.GET.get('environment_id'):
            data['id'] = request.GET.get('environment_id')

        qry_env = environment_service.filter(data).values_list('id', flat=True)

        if qry_env:
            filters['environment_id__in'] = list(qry_env)
        else:
            filters['environment_id'] = -1  #With this value, the filter will return no values.

    #Verify date section:
    
    start_date = datetime.min
    end_date   = datetime.max

    if request.GET.get('start_date'):
        start_date = datetime.strptime(request.GET.get('start_date'), "%m/%d/%Y")

    if request.GET.get('end_date'):
        end_date   = datetime.strptime(request.GET.get('end_date'), "%m/%d/%Y")

    filters['start_date__lte'] = end_date
    filters['end_date__gte']   = start_date

    return filters

#Este recibe como parametro un dict.
def getReservationFiltersDict(request):

    filters = {}

    if ('env_name' in request) or ('headquarter_id' in request) or ('environment_id' in request):

        environment_service = EnvironmentService()
        data = {}

        if 'env_name' in request:
            data['name__icontains'] = request['env_name']

        if 'headquarter_id' in request:
            data['headquarter_id'] = request['headquarter_id']

        if 'environment_id' in request:
            data['id'] = request['environment_id']

        qry_env = environment_service.filter(data).values_list('id', flat=True)

        if qry_env:
            filters['environment_id__in'] = list(qry_env)
        else:
            filters['environment_id'] = -1  #With this value, the filter will return no values.

    #Verify date section:
    
    start_date = datetime.min
    end_date   = datetime.max

    if 'start_date' in request:
        start_date = datetime.strptime(request['start_date'], "%m/%d/%Y")

    if 'end_date'   in request:
        end_date   = datetime.strptime(request['end_date'], "%m/%d/%Y")

    filters['start_date__lte'] = end_date
    filters['end_date__gte']   = start_date

    return filters

@require_http_methods(['GET'])
def create_reservation(request):

    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()

    context = {
        'titulo': 'tittle',
        'headquarters' : headquarters,
    }

    return render(request, 'Admin/Environments/Create_Reservation.html', context)


@require_http_methods(['POST'])
def create_reservation_post(request):

    environment_service = EnvironmentService()
    

    filters = getReservationFiltersDict(request.POST.dict())
    #return HttpResponse(filters['end_date__lte'])
    reservations = environment_service.filterReservations(filters)
    
    context = {
        'reservations' : reservations,
        'titulo'       : 'titulo'
    }

    #Si encuentra reserva alguna en la fecha no esta disponible
    if reservations.count() > 0 :
        return render_to_response('Admin/Environments/Create_not_available.html', context)   

    return render_to_response('Admin/Environments/Create_Reservation_Form.html', context)

@require_http_methods(['POST'])
def create_reservation_getEnvs(request):

    environment_service = EnvironmentService()

    environments = environment_service.filter({'headquarter_id' : request.POST.get('headquarter_id')})

    
    context = {
        'environments' : environments,
        'titulo' : 'titulo'
    }
    
    return render_to_response('Admin/Environments/Create_Reservation_Envs.html', context)

@require_http_methods(['POST'])
def insert_reservation(request):

    form = EnvReservationForm(request.POST)

    context = {
        'titulo': 'titulo'
    }

    request = FormValidator.validateForm(form, request)

    environment_service = EnvironmentService()

    if not request:

        

        price          = form.cleaned_data['price']
        start_date     = form.cleaned_data['start_date']
        end_date       = form.cleaned_data['end_date']
        environment_id = form.cleaned_data['environment_id']

        environment = environment_service.getEnviromentById(environment_id)

        insert_data = {
            'price'       : price,
            'start_date'  : start_date,
            'end_date'    : end_date,
            'environment' : environment,
            'status'      : 0
        }

        environment_service.createReservation(insert_data)

        return HttpResponse("index")

    else:
        return HttpResponse("create")
      

        """
        headquarter_service = HeadquarterService()

        headquarters = headquarter_service.getHeadquarters()

        context = {
            'headquarters' : headquarters,
            'titulo'       : 'titulo'
        }

        return render(request, 'Admin/Environments/Create_Reservation.html', context)
        """
