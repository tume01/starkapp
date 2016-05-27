from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.GuestService import GuestService
from django.views.decorators.http import require_http_methods
from Adapters.FormValidator import FormValidator
from .forms import GuestForm


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

    form = GuestForm(request.POST)

    request = FormValidator.validateForm(form, request)

    if not request:

        insert_data = {}

        insert_data["names"] = form.cleaned_data['names']

        insert_data["surnames"] = form.cleaned_data['surnames']

        insert_data["dni"] = form.cleaned_data['dni']

        insert_data["status"] = 1

        guest_service = GuestService()

        guest_service.create(insert_data)

        return HttpResponseRedirect(reverse('guests:index'))

    else:
        context = {
            'titulo': 'titulo'
        }

        return render(request, 'Guests/new_guests_members.html', context)


@require_http_methods(['POST'])
def edit_guest(request):

    form = GuestForm(request.POST)

    guest_service = GuestService()

    id_guest = request.POST['id']

    if FormValidator.validateForm(form, request):

        guest = guest_service.getGuest(id_guest)

        context = {
            'guest': guest,
        }

        return render(request, 'Guests/Edit_Guests_members.html', context)

    else:

        insert_data = {}

        insert_data["names"] = form.cleaned_data['names']

        insert_data["surnames"] = form.cleaned_data['surnames']

        insert_data["dni"] = form.cleaned_data['dni']

        guest_service = GuestService()

        guest_service.update(id_guest, insert_data)

        return HttpResponseRedirect(reverse('guests:index'))