from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.EventsService import EventsService
from services.EnvironmentService import EnvironmentService
from services.HeadquarterService import HeadquarterService
from services.EventsTypeService import EventsTypeService
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import EventForm
import datetime
from services.MemberService import MembersService
from django.conf import settings


@require_http_methods(['GET'])
def index(request):

    event_service = EventsService()

    filters = getActivityFilters(request)

    events = event_service.filter(filters)

    context = {
        'events' : events,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Events/index_event.html', context)


def getActivityFilters(request):

    filters = {}

    if request.GET.get('seat'):
        filters['seat'] = request.GET.get('seat')

    if request.GET.get('type'):
        filters['event_type_id'] = request.GET.get('type')

    if request.GET.get('status'):
        filters['status'] = request.GET.get('status')

    if request.GET.get('start_date'):
        start_date = datetime.datetime.strptime(request.GET.get('start_date'), "%m/%d/%Y")

        filters['start_date__gte'] = start_date

    if request.GET.get('end_date'):
        end_date = datetime.datetime.strptime(request.GET.get('end_date'), "%m/%d/%Y")

        filters['end_date__lte'] = end_date

    return filters


@require_http_methods(['GET'])
def create_index(request):

    environment_service = EnvironmentService()

    headquearter_service = HeadquarterService()

    eventstype_service = EventsTypeService()

    environments = environment_service.getEnvironment()

    headquarters = headquearter_service.getHeadquarters()

    eventstype = eventstype_service.getEventsType()

    context = {
        'titulo' : 'titulo',
        'environments' : environments,
        'headquarters' : headquarters,
        'eventstype' : eventstype
    }

    return render(request, 'Admin/Events/new_event.html', context)

@require_http_methods(['POST'])
@csrf_protect
def create_event(request):

    form = EventForm(request.POST, request.FILES)

    context = {
        'titulo' : 'titulo'
    }

    insert_data = {}


    if not form.is_valid():

        errors =  form.errors.as_data()

        for error in errors:

            validation_instance = errors[error]

            for instance_error in validation_instance:

                for error_message in instance_error:

                    messages.error(request,(error_message))

        return render(request,'Admin/Events/new_event.html',context)

    else:

        insert_data["name"] = form.cleaned_data.get('name')

        insert_data["description"] = form.cleaned_data.get('description')

        #insert_data["environment_id"] = form.cleaned_data.get('environment')

        member_service = MembersService()

        creator = member_service.getMemberByUser(request.user)

        insert_data["creator_id"] = creator.id

        insert_data["ruc"]  = request.POST.get('ruc')

        insert_data["headquarter_id"] = request.POST.get('headquarter')

        insert_data["start_date"] = form.cleaned_data.get("start_date","%Y/%m/%d")

        insert_data["end_date"] = form.cleaned_data.get("start_date","%Y/%m/%d")

        insert_data["assistance"] = request.POST.get('assistance')

        insert_data["price_member"] = request.POST.get('price_member')

        insert_data["price_invited"] = request.POST.get('price_invited')

        insert_data["status"] = 0

        insert_data["event_type_id"] = request.POST.get('event_type')

        insert_data["photo"] = request.FILES["photo"]

        event_service = EventsService()

        event_service.create(insert_data)

        return HttpResponseRedirect(reverse('events:index'))


@require_http_methods(['GET'])
def update_index(request,event_id):

    events_service = EventsService()


    filters = {
        'id' : event_id
    }

    events = events_service.filter(filters)

    context = {
        'titulo' : 'titulo',
        'events' : events,
    }

    return render(request,'Admin/Events/edit_event.html',context)


@require_http_methods(['POST'])
@csrf_protect
def update_events(request, event_id):

    form = EventForm(request.POST)

    context = {
        'titulo' : 'titulo'
    }

    insert_data = {}

    if request.POST.get('name'):
        insert_data["name"] = request.POST.get('name')

    if request.POST.get('description'):
        insert_data["description"] = request.POST.get('description')

    if request.POST.get('ruc'):
        insert_data["ruc"]  = request.POST.get('ruc')

    #if request.POST.get('environment'):

        #insert_data["environment_id"] = request.POST.get('environment')

    if request.POST.get('user'):

        insert_data["user_id"] = request.POST.get('user')

    if request.POST.get('seat'):
        insert_data["seat"] = request.POST.get('seat')

    if request.POST.get("start_date"):
        insert_data["start_date"] = datetime.datetime.strptime(request.POST.get("start_date"),"%m/%d/%Y %H:%M %p").date()

    if request.POST.get("end_date"):
        insert_data["end_date"] = datetime.datetime.strptime(request.POST.get("end_date"),"%m/%d/%Y %H:%M %p").date()

    if request.POST.get("assistance"):
        insert_data["assistance"] = request.POST.get("assistance")

    if request.POST.get('price'):
        insert_data["price"] = request.POST.get('price')

    if request.POST.get('event_type'):
        insert_data["event_type_id"] = request.POST.get('event_type')

    if request.POST.get('status'):
        insert_data["status"] = request.POST.get('status')

    events_service = EventsService()

    id_type = int('0' + event_id)

    events_service.update(id_type,insert_data)

    return HttpResponseRedirect(reverse('events:index'))

def index_registerUser(request, event_id):

    events_service = EventsService()

    event = events_service.getEvent(event_id)

    context = {
        'titulo' : 'titulo',
        'event' : event,
    }

    return render(request,'Admin/Events/register_attendant.html',context)

def registerUser(request, event_id):

    filters = {
        'document_number' : request.POST.get('document_number'),
        'paternalLastName': request.POST.get('paternalLastName'),
        'maternalLastName': request.POST.get('maternalLastName'),
        'name': request.POST.get('name'),
    }

    member_service = MembersService()

    users = member_service.filter(filters)

    if not users.count():
        messages.error(request,'Usuario no encontrado')
    else:

        event_service = EventsService()
        user = users[0]

        if event_service.registerMember(event_id, user):
            messages.success(request, 'Usuario anadido al evento')
            return HttpResponseRedirect(reverse('events:registrations', args=[event_id]))

        messages.error(request, 'Error al anadir Usuario')

    return HttpResponseRedirect(reverse('events:register_index', args=[event_id]))

def registrations(request, event_id):

    event_service = EventsService()

    registrations = event_service.getEventRegistrations(event_id)

    context = {
        'registrations' : registrations,
        'event_id' : event_id
    }

    return render(request, 'Admin/Events/registrations.html', context)

def removeUser(request, event_id, member_id):

    event_service = EventsService()

    if event_service.removeUserRegistration(event_id, member_id):
        messages.success(request, 'Miembro removido de evento correctamente')
    else:
        messages.error(request, 'Miembro no puede ser removido con menos de 1 semana de anticipacion')

    return HttpResponseRedirect(reverse('events:registrations', args=[event_id]))

def index_UserEvents(request):

    member_service = MembersService()

    user_events = member_service.getUserEvents(request.user)

    context = {
        'registrations': user_events
    }

    return render(request, 'User/Events/myEvents.html', context)

def index_UserSignup(request):

    event_service = EventsService()
    eventstype_service = EventsTypeService()

    events = event_service.getEvents()
    event_types = eventstype_service.getEventsType()

    context = {
        'events': events,
        'event_types': event_types,
        'image_url': settings.MEDIA_URL
    }

    return render(request, 'User/Events/index.html', context)

def select_userEvent(request, event_id):

    event_service = EventsService()

    event = event_service.getEvent(event_id)

    context = {
        'event': event,
        'image_url': settings.MEDIA_URL
    }

    return render(request, 'User/Events/select.html', context)

def userSignup(request, event_id):

    member_service = MembersService()
    event_service = EventsService()

    member = member_service.getMemberByUser(request.user)

    if event_service.registerMember(event_id, member):
        messages.success(request, 'Inscripcion en evento exitosa')
        return HttpResponseRedirect(reverse('events:userEvents_index'))

    messages.error(request, 'Error al inscribirse en el evento')

    return HttpResponseRedirect(reverse('events:userEvent_select', args=[event_id]))

def userSignout(request, event_id):

    event_service = EventsService()
    member_service = MembersService()

    member = member_service.getMemberByUser(request.user)

    if event_service.removeUserRegistration(event_id, member.id):
        messages.success(request, 'Miembro removido de evento correctamente')
    else:
        messages.error(request, 'Miembro no puede ser removido con menos de 1 semana de anticipacion')

    return HttpResponseRedirect(reverse('events:userEvents_index'))

def checkoutEvent(request, event_id):

    guests = request.POST.get('guests', 0)

    member_service = MembersService()
    member = member_service.getMemberByUser(request.user)

    event_service = EventsService()

    event =environment_service.getEvent(event_id)

    checkout_products = payment_service.createCheckoutProducts(products,member)

    return HttpResponseRedirect(reverse('payments:checkout_preview'))