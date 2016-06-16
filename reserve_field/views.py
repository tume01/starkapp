from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.EnvironmentService import EnvironmentService
from django.views.decorators.http import require_http_methods
from services.HeadquarterService import HeadquarterService
from services.FieldReservationService import FieldReservationService
from services.MemberService import MembersService
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import JsonResponse

import datetime

@require_http_methods(['GET'])
def index(request):

    environment_service = EnvironmentService()
    headquarter_service = HeadquarterService()


    filters = {
        'environment_type_id' : 7,
    }

    fields = environment_service.filter(filters)
    stay_max_hours = {1,2,3}

    hours = ['08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00']

    context = {
        'fields' : fields,
        'titulo' : 'titulo',
        'stay_max_hours' : stay_max_hours,
        'headquarters' : headquarter_service.getHeadquarters(),
        'hours' :   hours
    }

    return render(request, 'User/Reservation/fields.html', context)

@require_http_methods(['GET'])
def create_index_admin(request):
    context = {
        'headquarters': HeadquarterService().getHeadquarters(),
        'titulo': 'titulo'
    }

    return render(request, 'Admin/courtReservation/reserve_court.html', context)

@require_http_methods(['POST'])
def refresh_events(request):

    month = int(request.POST['start'])
    year = int(request.POST['end'])

    headquarter_id = int(request.POST['headquarter_id'])

    court_type_id  = int(request.POST['court_type_id'])

    environment_type = 1 #default for courts

    environment_service = EnvironmentService()
    
    courts = environment_service.getEnvironment()

    courts = courts.filter(environment_type_id=environment_type)

    if (headquarter_id != -1):

        print("Filter by Headquarter_ID")
        courts = courts.filter(headquarter_id=headquarter_id)

    if (court_type_id != -1):

        print("Filter by court_type_id")
        courts = courts.filter(court_type=court_type_id)


    #availableDays = FieldReservationService.getDayAvailableHours(1, month, year)


    context = {
        'courts': courts
    }

    return JsonResponse({'events':[
        {
            'title': 'Dinner',
            'start': '2016-06-14T22:00:00'
        },
        {
            'title': 'Birthday Party',
            'start': '2016-06-15T22:00:00'
        },
    ]})

@require_http_methods(['POST'])
@csrf_protect
def refresh_field(request):
    arrival_date = request.POST.get('arrival_date')
    headquarter_id = int(request.POST.get('headquarter_id'))


    environment_service = EnvironmentService()

    filters = {
        'arrival_date' : arrival_date,
        'headquarter_id' : headquarter_id,
        'environment_type_id' : 7
    }

    if (headquarter_id != -1):
        print("Filter by Headquarter_ID")
        headquarter_filter={
            'headquarter_id' : headquarter_id
        }
        fields = environment_service.filter(headquarter_filter)

    if (arrival_date != ""):
        print("Filter if available")
        fields = environment_service.filter(filters)

    context = {
        'fields': fields
    }

    return render_to_response('User/Reservation/combo_fields.html', context)

@require_http_methods(['POST'])
@csrf_protect
def refresh_hour(request):

    environment = request.POST['environment_content']

    field_reservation_service   = FieldReservationService()

    filters = {
        'court_name'  : environment   
    }

    hours = ['08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00']

    court_date = field_reservation_service.filter(filters)

    for court in court_date:
        if court.reservation_hour in hours:
            hours.remove(court.reservation_hour)
        if (court.reservation_hour + court.reservation_duration - 1) in hours:
            hours.remove(court.reservation_hour + court.reservation_duration - 1)

    context = {
        'hours' : hours
    }

    return render_to_response('User/Reservation/combo_hour.html', context)

@require_http_methods(['POST'])
@csrf_protect
def refresh_max_time(request):

    field_reservation_service   = FieldReservationService()

    environment = request.POST['environment_content']

    filters = {
        'court_name'  : environment
    }

    current_court = field_reservation_service.filter(filters)

    hours_reservated = []

    for court in current_court:
        hours_reservated.append(court.reservation_hour)

    start_hour = request.POST['start_hour']

    max_hours = [1,2]

    stay_max_hours = []

    for hour in max_hours:
        if(hour + start_hour) not in hours_reservated:
            stay_max_hours.append(hour)

    context = {
        'stay_max_hours' : stay_max_hours
    }

    return render_to_response('User/Reservation/combo_hour.html', context)

@require_http_methods(['POST'])
@csrf_protect
def reservate_court(request):

    headquarter_service = HeadquarterService()

    insert_data = {}

    insert_data['court_name']               = request.POST.get('environment_content')
    headquarter_id                          = request.POST.get('headquarter_id')

    headquarter                             = headquarter_service.findHeadquarter(headquarter_id)
    insert_data['court_headquarter_name']   = headquarter.name


    insert_data['reservation_hour']         = request.POST.get('start_hour')
    insert_data['reservation_duration']     = request.POST.get('stay_content')
    insert_data['reservation_date']         = datetime.datetime.strptime(request.POST.get('arrival_date'),"%m/%d/%Y").date()

    member_service                          = MembersService()
    user                                    = member_service.getMemberByUser(request.user)
    
    insert_data['member_membership_name']   = user.membership
    insert_data['member_name']              = user.name
    insert_data['member_paternalLastName']  = user.paternalLastName
    insert_data['member_maternalLastName']  = user.maternalLastName

    insert_data['status']                   = 1

    field_reservation_service               = FieldReservationService()

    field_reservation_service.create(insert_data)

    context={
        'success' : 'El evento ha sido registrado de manera correcta'
    }

    return render(request, 'User/Reservation/fields.html', context)