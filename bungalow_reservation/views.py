from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from services.BungalowReservationService import BungalowReservationService

from services.BungalowTypeService import BungalowTypeService
from services.HeadquarterService import HeadquarterService
from services.MemberService import MembersService
from services.BungalowService import BungalowService
from services.Bungalow_serviceService import Bungalow_serviceService


from bungalow_reservation.models import BungalowReservation
import datetime
from django.http import JsonResponse
import json


@require_http_methods(['GET'])
def index(request):
    reservations = BungalowReservationService.getReservations()

    paginator = Paginator(reservations, 10)
    page = request.GET.get('page')

    try:
        paginated = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_reservations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_reservations = paginator.page(paginator.num_pages)

    context = {
        'reservations': paginated_reservations,
        'bungalowTypes': BungalowTypeService.getBungalowTypes(),
        'headquarters': HeadquarterService().getHeadquarters(),
        'status_choices': BungalowReservation.STATUS_CHOICES,
        'titulo': 'titulo'
    }

    return render(request, 'Admin/bungalowReservation/index.html', context)


@require_http_methods(['POST'])
def refresh_table(request):
    # bungalow_type_id = int(request.POST['bungalow_type_id'])
    headquarter_id = int(request.POST['headquarter_id'])
    status = int(request.POST['status'])

    page = 1
    if 'page' in request.POST:
        page = int(request.POST['page'])

    reservations = BungalowReservationService.getReservations()
    print([r.bungalow_id for r in reservations])
    if (status != -1):
        print("Filter by Status")
        reservations = reservations.filter(status=status)

    if (headquarter_id != -1):
        print("Filter by Headquarter_ID")
        headquarter_name = HeadquarterService().findHeadquarter(headquarter_id).name
        reservations = [reservation for reservation in reservations if
                        reservation.bungalow_headquarter_name == headquarter_name]

    paginator = Paginator(reservations, 10)
    paginated_reservations = paginator.page(page)

    context = {
        'reservations': paginated_reservations,
    }

    return render_to_response('Admin/bungalowReservation/index_table.html', context)


@require_http_methods(['POST'])
def check_in(request):
    reservation_id = request.POST['reservation_id']

    insert_data = {}
    insert_data["check_in"] = datetime.datetime.now()
    insert_data["status"] = 2

    BungalowReservationService.update(reservation_id, insert_data)

    return HttpResponse("Success")


@require_http_methods(['POST'])
def check_out(request):
    reservation_id = request.POST['reservation_id']

    insert_data = {}
    insert_data["check_out"] = datetime.datetime.now()
    insert_data["status"] = 4

    BungalowReservationService.update(reservation_id, insert_data)

    return HttpResponse("Success")


@require_http_methods(['POST'])
def accept(request):
    reservation_id = request.POST['reservation_id']

    insert_data = {}
    insert_data["status"] = 1

    BungalowReservationService.update(reservation_id, insert_data)

    return HttpResponse("Success")


@require_http_methods(['POST'])
def cancel(request):
    reservation_id = request.POST['reservation_id']

    insert_data = {}
    insert_data["deleted_at"] = datetime.datetime.now()

    BungalowReservationService.update(reservation_id, insert_data)

    return HttpResponse("Success")


@require_http_methods(['GET'])
def create_index(request):
    context = {
        'headquarters': HeadquarterService().getHeadquarters(),
        'bungalowTypes': BungalowTypeService().getBungalowTypes(),
        'titulo': 'titulo'
    }
    return render(request, 'Admin/bungalowReservation/reserve_bungalow.html', context)

@require_http_methods(['POST'])
def create_refresh_events(request):
    start = int(request.POST['start'])
    end = int(request.POST['end'])

    bungalow_type_id = int(request.POST['bungalow_type_id'])
    headquarter_id = int(request.POST['headquarter_id'])
    availableDays = BungalowReservationService.getMonthAvailableDaysBF(headquarter_id, bungalow_type_id, start, end)
    response = {
        'events': availableDays
    }
    return JsonResponse(response)


@require_http_methods(['GET'])
def create_reserve_index(request):

    bungalow_id = request.GET.get('bungalow_id')
    bungalow = BungalowService.findBungalow(bungalow_id)
    date = datetime.datetime.fromtimestamp(int(request.GET.get('date')))

    bungalowTypes = BungalowTypeService.getBungalowTypes()
    headquarters = HeadquarterService().getHeadquarters()

    reservation = BungalowReservation()
    reservation.bungalow_id = bungalow.id
    reservation.bungalow_price = bungalow.bungalow_type.price
    reservation.bungalow_capacity = bungalow.bungalow_type.capacity
    reservation.bungalow_type_id = bungalow.bungalow_type.id
    reservation.bungalow_headquarter_id = bungalow.headquarter.id
    reservation.bungalow_headquarter_name = bungalow.headquarter.name

    reservation.arrival_date = date

    context = {
        'reservation': reservation,
        'bungalowTypes': bungalowTypes,
        'headquarters': headquarters,
        'durationOptions': [1,2,3,4],
        'titulo': 'titulo'
    }

    return render(request, 'Admin/bungalowReservation/reserve_bungalow_part2.html', context)


def create_reserve(request):


    print("POST CREATE RESERVE")
    print(request.POST)
    insert_data = {}


    bungalow = BungalowService.findBungalow(request.POST['bungalow_id'])
    member = MembersService().getMemberByUserId(request.user)
    arrival_date = datetime.datetime.strptime(request.POST['arrival_date'], '%d/%m/%Y')
    departure_date = arrival_date + datetime.timedelta(days=int(request.POST['duration']))


    insert_data["status"] = 0

    insert_data["bungalow_id"] = bungalow.id
    insert_data["bungalow_number"] = bungalow.number
    insert_data["bungalow_price"] = bungalow.bungalow_type.price
    insert_data["bungalow_capacity"] = bungalow.bungalow_type.capacity
    insert_data["bungalow_type_id"] = bungalow.bungalow_type.id

    insert_data["bungalow_headquarter_id"] = bungalow.headquarter.id
    insert_data["bungalow_headquarter_name"] = bungalow.headquarter.name

    insert_data["member_id"] = member.id
    insert_data["member_name"] = member.name
    insert_data["member_membership_name"] = member.membership.membership_type.name
    insert_data["member_paternalLastName"] = member.paternalLastName
    insert_data["member_maternalLastName"] = member.maternalLastName

    insert_data["arrival_date"] = arrival_date
    insert_data["departure_date"] = departure_date

    BungalowReservationService.create(insert_data)
    return HttpResponseRedirect(reverse('bungalowReservation:index'))


@require_http_methods(['GET'])
def update_index(request, bungalow_id):
    pass


@require_http_methods(['POST'])
def update_bungalow(request, bungalow_id):
    pass

@require_http_methods(['GET'])
def aditionalServiceBungalowIndex(request):
    members_service = MembersService()
    bungalow_reservation_service = BungalowReservationService()

    member = members_service.filter({'user_id':request.user.id}).first()
    print("member id = ")
    print(member.id)

    reservationsByMember = bungalow_reservation_service.getReservationsByMember(member.id)
    print("number reservations")
    print(reservationsByMember[1])

    context = {
        'reservations' : reservationsByMember,
        'bungalow_services': Bungalow_serviceService.getBungalow_services(),
        'titulo': 'titulo'
    }
    return render(request, 'User/bungalowReservation/aditionalService.html', context)

@require_http_methods(['POST'])
def filterAditionalServiceBungalow(request, id):
    req = json.loads( request.body.decode('utf-8') )

    bungalow = BungalowService.findBungalow(id)

    print((bungalow.bungalow_type).bungalow_services)

    return HttpResponse( json.dumps(req), content_type='application/json')

