from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.PromotionsService import PromotionsService
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST'])
def index(request):

    guest_service = GuestService()

    """
    no se como van a manejar esto pero necesito solo los invitados
    del usuario que se ha logueado
      
    userId = user_service.getId()
    """
    userId = 1

    filter_guest = {}

    filter_guest["iniDate"] = request.POST['iniDate']

    filter_guest["endDate"] = request.POST['endDate']

    filter_guest["sede"] = request.POST['sede']

    guests = guest_service.getGuests(userId, filter_guest)

    """
    guests debe tener:
    id, nombres, apellidos, dni de la tabla guest
    ingreso, salida de la tabla ingreso ingreso
    sede que es el nombre de la tabla sede
    """

    context = {
        'guests' : guests,
    }

    return render(request, 'Guests/Guests_member.html', context) 


@require_http_methods(['GET'])
def create_index(request):

    return render(request, 'Guests/New_Guests_members.html', context)

@require_http_methods(['GET'])
def edit_index(request):

    guest_service = GuestService()

    """
    no se como van a manejar esto pero necesito solo los invitados
    del usuario que se ha logueado
      
    userId = user_service.getId()
    """
    userId = 1

    guest = guest_service.getGuest(userId)

    context = {
        'guest' : guest,
    }

    return render(request, 'Guests/Edit_Guests_members.html', context)

@require_http_methods(['POST'])
def delete_guest(request):

    insert_data = {}

    insert_data["id"] = request.POST['id']

    insert_data["estado"] = 0

    guest_service = GuestService()

    guest_service.update(insert_data)

    return HttpResponseRedirect(reverse('guests:index'))


@require_http_methods(['POST'])
def create_guest(request):

    insert_data = {}

    insert_data["nombres"] = request.POST['nombres']

    insert_data["apellido"] = request.POST['apellido']

    insert_data["dni"] = request.POST['dni']

    insert_data["estado"] = 1

    guest_service = GuestService()

    guest_service.create(insert_data)

    return HttpResponseRedirect(reverse('guests:index'))


@require_http_methods(['POST'])
def edit_guest(request):

    insert_data = {}

    insert_data["nombres"] = request.POST['nombres']

    insert_data["apellido"] = request.POST['apellido']

    insert_data["dni"] = request.POST['dni']

    insert_data["id"] = request.POST['id']

    guest_service = GuestService()

    guest_service.update(insert_data)

    return HttpResponseRedirect(reverse('guests:index'))