from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.EnvironmentService import EnvironmentService
from django.views.decorators.http import require_http_methods
from services.HeadquarterService import HeadquarterService
from services.FieldReservationService import FieldReservationService


@require_http_methods(['GET'])
def index(request):

    environment_service = EnvironmentService()
    headquarter_service = HeadquarterService()


    filters = {
        'environment_type_id' : 1,
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


@require_http_methods(['POST'])
def refresh_field(request):

    arrival_date = request.POST['arrival_date']
    headquarter_id = int(request.POST['headquarter_id'])

    environment_service = EnvironmentService()

    filters = {
        'arrival_date' : arrival_date,
        'headquarter_id' : headquarter_id,
        'environment_type_id' : 1
    }


    if (headquarter_id != -1):
        print("Filter by Headquarter_ID")
        fields = environment_service.filter(headquarter_id=headquarter_id)

    if (arrival_date != ""):
        print("Filter if available")
        fields = environment_service.filter(filters)

    context = {
        'fields': fields
    }

    return render_to_response('User/Reservation/combo_fields.html', context)

@require_http_methods(['POST'])
def refresh_hour(request):

    environment = request.POST['environment_content']

    environment_service = EnvironmentService()
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
def refresh_max_time(request):

    stay_time = request.POST['stay_content']

    field_reservation_service   = FieldReservationService()

    content = {
        ''

    }

    return render_to_response('User/Reservation/combo_hour.html', context)
