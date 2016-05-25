from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.GuestService import GuestService
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Guests/new_guests_members.html', context)

@require_http_methods(['GET'])
def edit_index(request):

    guest_service = GuestService()

    id_guest = request.POST['id']

    guest = guest_service.getGuest(id_guest)

    context = {
        'guest' : guest,
    }

    return render(request, 'Guests/Edit_Guests_members.html', context)


@require_http_methods(['POST'])
def create_guest(request):

    insert_data = {}

    insert_data["names"] = request.POST['names']

    insert_data["surnames"] = request.POST['surnames']

    insert_data["dni"] = request.POST['dni']

    insert_data["status"] = 1

    guest_service = GuestService()

    guest_service.create(insert_data)

    return HttpResponseRedirect(reverse('guests:index'))


@require_http_methods(['POST'])
def edit_guest(request):

    insert_data = {}

    insert_data["names"] = request.POST['names']

    insert_data["surnames"] = request.POST['surnames']

    insert_data["dni"] = request.POST['dni']

    id_guest = request.POST['id']

    guest_service = GuestService()

    guest_service.update(id_guest, insert_data)

    return HttpResponseRedirect(reverse('guests:index'))