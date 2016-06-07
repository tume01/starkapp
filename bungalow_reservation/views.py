from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from services.BungalowReservationService import BungalowReservationService

from bungalow_reservation.models import BungalowReservation
from bungalow.models import Bungalow
import datetime

@require_http_methods(['GET'])
def index(request):

    reservations = BungalowReservationService.getReservations()

    context = {
        'reservations' : reservations,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/bungalowReservation/index.html', context)

@require_http_methods(['POST'])
def index_filters(request):

    from django.core import serializers

    bungalow_type_id = request.POST['bungalow_type_id']
    member_name = request.POST['member_name']
    headquarter_id = request.POST['headquarter_id']
    
    reservations = BungalowReservationService.getReservations()


    if (bungalow_type_id != -1):
        reservations = [reservations for reservations.bungalow.bungalow_type_id in [bungalow_type_id]]
    # if (headquarter_id != -1):
    #     bungalows = bungalows.filter(headquarter_id = headquarter_id)

    context = {
        'reservations' : reservations
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

    BungalowReservationService.update(reservation_id, insert_data)

    return HttpResponse("Success")


@require_http_methods(['GET'])
def create_index(request):
    pass


@require_http_methods(['POST'])
def create_bungalow(request):
    pass



@require_http_methods(['GET'])
def update_index(request, bungalow_id):
    pass


@require_http_methods(['POST'])
def update_bungalow(request, bungalow_id):

    pass