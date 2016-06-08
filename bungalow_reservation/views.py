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

from bungalow_reservation.models import BungalowReservation
import datetime


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

    BungalowReservationService.update(reservation_id, insert_data)

    return HttpResponse("Success")


@require_http_methods(['POST'])
def check_out(request):
    reservation_id = request.POST['reservation_id']

    insert_data = {}
    insert_data["check_out"] = datetime.datetime.now()
    insert_data["status"] = 0

    BungalowReservationService.update(reservation_id, insert_data)

    return HttpResponse("Success")


@require_http_methods(['GET'])
def create_index(request):
    pass


@require_http_methods(['POST'])
def create_bungalow_reservation(request):
    insert_data = {}

    insert_data["bungalow_id"] = request.POST['bungalow_id']
    insert_data["member_id"] = request.POST['member_id']
    insert_data["status"] = request.POST['status']

    bungalowTypeId = request.POST['bungalow_type_id']
    insert_data["bungalow_type"] = BungalowTypeService.findBungalowType(bungalowTypeId)

    BungalowReservationService.create(insert_data)

    return HttpResponseRedirect(reverse('bungalow:index'))


@require_http_methods(['GET'])
def update_index(request, bungalow_id):
    pass


@require_http_methods(['POST'])
def update_bungalow(request, bungalow_id):
    pass
