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
from services.HeadquarterService import HeadquarterService
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@require_http_methods(['GET'])
def index(request):

    environment_service = EnvironmentService()

    environments = environment_service.getEnvironmentByStatus()

    context = {
        'environments' : environments,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/List_Environment.html', context)


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/Create_Environment.html', context)

@require_http_methods(['POST'])
def edit_index(request):

    id_environment= request.POST['id']

    environment_service = EnvironmentService()

    environment = environment_service.getEnviromentById(id_environment)

    context = {

        'environment' : environment,
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

    insert_data = {}

    insert_data["name"] = request.POST['name']

    #insert_data["sede"] = request.POST['sede']

    insert_data["description"] = request.POST['description']

    insert_data["status"] = 1

    insert_data["capacity"] = request.POST['capacity']

    #insert_data["environment_id"] = request.POST['number']

    environment_service = EnvironmentService()

    environment_service.create(insert_data)

    return HttpResponseRedirect(reverse('environment:index'))


@require_http_methods(['POST'])
def edit_environment(request):

    edit_data = {}

    edit_data["description"] = request.POST['description']

    edit_data["name"] = request.POST['name']

    edit_data["capacity"] = request.POST['capacity']

    edit_data["status"] = request.POST['status']

    id_edit = request.POST['id']

    environment_service = EnvironmentService()

    environment_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('environment:index'))


# Metodos para la reserva de ambientes

@require_http_methods(['GET'])
def index_book(request):

    environment_service = EnvironmentService()
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()

    filters = getReservationFilters(request)
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
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/List_Reservations.html', context)


def getReservationFilters(request):


    filters = {}

    if request.GET.get('env_name') || request.GET.get('headquarter_id'):

        environment_service = EnvironmentService()
        data = {}

        if request.GET.get('env_name'):
            data['name__icontains'] = request.GET.get('env_name')

        if request.GET.get('headquarter_id'):
            data['headquarter_id'] = request.GET.get('headquarter_id')

        env_tmp = environment_service.filter(data).first()
        if env_tmp:
            filters['environment_id'] = env_tmp.id

    if request.GET.get('start_date'):
        start_date = datetime.strptime(request.GET.get('start_date'), "%m/%d/%Y")

        filters['start_date__gte'] = start_date

    if request.GET.get('end_date'):
        end_date = datetime.strptime(request.GET.get('end_date'), "%m/%d/%Y")

        filters['end_date__lte'] = end_date

    return filters

@require_http_methods(['GET'])
def create_reservation(request):

    environments_service = EnvironmentService()
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()
    environments = environments_service.getEnvironment()

    context = {
        'titulo': 'tittle',
        'environments': environments,
        'headquarters' : headquarters
    }

    return render(request, 'Admin/Environments/Create_Reservation.html', context)


@require_http_methods(['GET'])
def create_reservation_post(request):

    environment_service = EnvironmentService()

    filters = getReservationFilters(request)
    reservations = environment_service.filterReservations(filters)

    
    context = {
        'reservations' : reservations,
        'titulo' : 'titulo'
    }

    #Si encuentra reserva alguna en la fecha no esta disponible
    if reservations.count() > 0 :
        return render(request, 'Admin/Environments/Create_not_available.html', context)   

    return render(request, 'Admin/Environments/Create_Reservation_Form', context)

@require_http_methods(['POST'])
def insert_reservation(request):

    form = EnvReservationForm(request.POST)

    context = {
        'titulo': 'titulo'
    }

    request = FormValidator.validateForm(form, request)

    environment_service = EnvironmentService()

    if not request:

        

        price = form.cleaned_data['price']
        start_date = form.cleaned_data['start_date']
        end_date   = form.cleaned_data['end_date']
        enviroment_id = form.cleaned_data['enviroment_id']

        enviroment = environments_service.getEnviromentById(enviroment_id)

        insert_data = {
            'price'      : price,
            'start_date' : start_date,
            'end_date'   : end_date,
            'enviroment' : enviroment
        }

        environment_service.createReservation(insert_data)

        return HttpResponseRedirect(reverse('enviroment:index_book'))

    else:
        
        headquarter_service = HeadquarterService()

        headquarters = headquarter_service.getHeadquarters()
        environments = environments_service.getEnvironment()

        context = {
            'reservations' : reservations,
            'headquarters' : headquarters,
            'titulo'       : 'titulo'
        }

        return render(request, 'Admin/Activities/Create_Reservation.html', context)