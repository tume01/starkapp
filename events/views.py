from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.EventsService import EventsService
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import EventForm
import datetime

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

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Events/new_event.html', context)

@require_http_methods(['POST'])
@csrf_protect
def create_event(request):

    form = EventForm(request.POST)

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

        insert_data["ruc"]  = request.POST.get('ruc')

        insert_data["seat"] = request.POST.get('seat')
     
        insert_data["start_date"] = form.cleaned_data.get("start_date","%Y/%m/%d")

        insert_data["end_date"] = form.cleaned_data.get("start_date","%Y/%m/%d")   

        insert_data["assistance"] = request.POST.get('assistance')

        insert_data["price"] = request.POST.get('price')

        insert_data["status"] = 0

        insert_data["event_type_id"] = request.POST.get('event_type')

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
        'events' : events
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