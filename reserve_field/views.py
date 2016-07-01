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

    court_reservation_service = FieldReservationService()

    member_service = MembersService()
    member = member_service.getMemberByUser(request.user)

    member_id = member.id

    filters = {
        'member_id' : member_id
    }

    reservations = court_reservation_service.filter(filters)

    context = {
        'reservations' : reservations,
    }

    return render(request, 'User/courtReservation/index.html', context)

@require_http_methods(['GET'])
def create_index_admin(request):
    context = {
        'headquarters': HeadquarterService().getHeadquarters(),
        'titulo': 'titulo'
    }

    return render(request, 'User/courtReservation/reserve_court.html', context)

@require_http_methods(['POST'])
def refresh_events(request):

    start = int(request.POST['start'])
    end = int(request.POST['end'])

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

    court_reservation_services = FieldReservationService()


    availableHours = court_reservation_services.getDayAvailableHours(courts,headquarter_id ,court_type_id, start, end)

    response = {
        'events': availableHours
    }

    return JsonResponse(response)


@require_http_methods(['GET'])
def court_show(request):
    headquarter_id  = request.GET.get('headquarter')
    court_type      = int(request.GET.get('court_type'))
    fullDate        = request.GET.get('date')
    date            = request.GET.get('date').split('T')



    headquarter_service = HeadquarterService()
    headquarter = headquarter_service.findHeadquarter(headquarter_id)

    print(court_type)

    context = {
        'headquarter' : headquarter,
        'court_type'  : court_type,
        'max_hours'   : [1,2],
        'date'        : date[1],
        'fullDate'    : fullDate
    }


    return render(request,'User/courtReservation/fields_part2.html',context)


@require_http_methods(['POST'])
def reservate_court(request):

    headquarter_service = HeadquarterService()

    insert_data = {}

    fullDate                                = request.POST.get('date').split('T')

    day                                     = fullDate[0].split('-')
    hour                                    = fullDate[1].split(':')

    headquarter_id                          = request.POST.get('headquarter_id')

    headquarter                             = headquarter_service.findHeadquarter(headquarter_id)
    insert_data['headquarter_id']           = headquarter.id
    insert_data['court_headquarter_name']   = headquarter.name

    court_type                              = request.POST.get('court_type')
    insert_data['court_type']               = court_type
    if court_type == 0:
        insert_data['court_name']           = "Cancha de Fútbol"
    elif court_type == 1:
        insert_data['court_name']           = "Cancha de Básquet"
    else :
        insert_data['court_name']           = "Cancha de Tenis"

    insert_data['reservation_duration']     = request.POST.get('court_duration')
    insert_data['reservation_date']         = datetime.datetime(int(day[0]),int(day[1]),int(day[2]),int(hour[0]),int(hour[1]),int(hour[2]))

    member_service                          = MembersService()
    user                                    = member_service.getMemberByUser(request.user)

    insert_data['member_id']                = user.id
    insert_data['member_membership_name']   = user.membership
    insert_data['member_name']              = user.name
    insert_data['member_paternalLastName']  = user.paternalLastName
    insert_data['member_maternalLastName']  = user.maternalLastName

    insert_data['status']                   = 1

    field_reservation_service               = FieldReservationService()

    filters()

    court = field_reservation_service.filter()

    if(insert_data['reservation_date'] == )

    field_reservation_service.create(insert_data)

    context={
        'success' : 'El evento ha sido registrado de manera correcta'
    }

    return HttpResponseRedirect(reverse('reserve_field:index'))