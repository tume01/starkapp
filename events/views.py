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

    events = event_service.getEvents()

    context = {
        'events' : events,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Events/index_event.html', context) 

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

        return HttpResponseRedirect(reverse('events:index'))


    # form_name.er

    # insert_data["description"] = request.POST.get('description')
 
    # insert_data["start_date"] = datetime.datetime.strptime(request.POST.get('start_date'),"%Y-%m-%d").date()

    # insert_data["end_date"] = datetime.datetime.strptime(request.POST.get('end_date'),"%Y-%m-%d").date()

    # insert_data["assistance"] = 20

    # insert_data["price"] = request.POST.get('price')

    # insert_data["status"] = 1

    # insert_data["event_type_id"] = 1

    # event_service = EventsService()

    # event_service.create(insert_data)

    return HttpResponseRedirect(reverse('events:index'))