from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.EventsTypeService import EventsTypeService
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import EventsTypeForm
import datetime

@require_http_methods(['GET'])
def index(request):

    events_type_service = EventsTypeService()

    events_type = events_type_service.getEventsType()

    context = {
        'events_type' : events_type,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Events_type/index_events_type.html', context) 

@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Events_type/new_events_type.html', context)

@require_http_methods(['POST'])
@csrf_protect
def create_eventstype(request):

    form = EventsTypeForm(request.POST)

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

        return render(request,'Admin/Events_type/new_events_type.html',context)

    else:

        insert_data["name"] = request.POST.get('name')

        insert_data["description"] = request.POST.get('description')

        insert_data["status"] = 1

        events_type_service = EventsTypeService()

        events_type_service.create(insert_data)

        return HttpResponseRedirect(reverse('events_type:index'))
