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

    availableDays = BungalowReservationService.getMonthAvailableDays(headquarter_id, bungalow_type_id, start, end)
    response = {
        'events': availableDays
    }
    return JsonResponse(response)


@require_http_methods(['GET'])
def create_reserve_index(request):

    bungalow_type_id = request.GET.get('bungalow_type_id')
    headquarter_id = request.GET.get('headquarter_id')
    date = datetime.datetime.fromtimestamp(int(request.GET.get('date')))

    bungalow_type = BungalowTypeService.findBungalowType(bungalow_type_id)
    bungalowTypes = BungalowTypeService.getBungalowTypes()
    headquarter = HeadquarterService().findHeadquarter(headquarter_id)
    headquarters = HeadquarterService().getHeadquarters()

    reservation = BungalowReservation()
    reservation.bungalow_price = bungalow_type.price
    reservation.bungalow_capacity = bungalow_type.capacity
    reservation.bungalow_type_id = bungalow_type.id
    reservation.bungalow_headquarter_id = headquarter.id
    reservation.bungalow_headquarter_name = headquarter.name

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
    insert_data = {}
    print(request.POST)
    bungalow_type_id = request.POST['bungalow_type_id']
    # member_id = request.POST['member_id']

    # insert_data["arrival_date"] = request.POST['arrival_date']
    # insert_data["departure_date"] = request.POST['departure_date']
    #
    # insert_data["status"] = 0
    #
    # bungalow = BungalowService.findBungalow(bungalow_id)
    # insert_data["arrival_date"] = request.POST['arrival_date']
    # insert_data["bungalow_number"] = bungalow.number
    # insert_data["bungalow_price"] = bungalow.bungalow.bungalow_type.price
    # insert_data["bungalow_capacity"] = bungalow.bungalow_type.capacity
    # insert_data["bungalow_headquarter_name"] = bungalow.headquarter.name
    #
    # member = MembersService().getMember(member_id)
    # insert_data["membership_name"] = member.membership.membership_type.name
    # insert_data["name"] = member.name
    # insert_data["paternalLastName"] = member.paternalLastName
    # insert_data["maternalLastName"] = member.maternalLastName

    # BungalowReservationService.create(insert_data)
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

