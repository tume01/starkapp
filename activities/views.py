from datetime import datetime
from .forms import ActivityForm
from django.template import loader
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.ActivityService import ActivityService 
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def index(request):

    context = {
        'titulo' : 'tittle'
    }

    return render(request, 'Admin/Activities/index_activity.html', context)

@require_http_methods(['POST'])
def create_activity(request):
    
    form = ActivityForm(request.POST)

    context = {
        'titulo' : 'titulo'
    }

    if form.is_valid():

        errors = form.errors.as_data()

        for error in errors:

            validation_instance = errors[error]

            for instance_error in validation_instance:

                for error_message in instance_error:

                    messages.error(request, (error_message))

        return render(request, 'Admin/Activities/new_activity.html', context)

    else:
        return HttpResponseRedirect(reverse('activities:index'))
        


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'tittle'
    }

    return render(request, 'Admin/Activities/new_activity.html', context)

@require_http_methods(['POST'])
def delete(request):
    pass


@require_http_methods(['GET'])
def update_index(request):
    
    context = {
        'titulo' : 'tittle'
    }

    activity_service = ActivityService()

    update_data = {}

    update_data["start_date"] = datetime(2015, 1, 1)
    update_data["end_date"] = datetime(2015, 2, 2)
    update_data["attendance"] = 2
    update_data["price"] = 2

    filters = {
        "price" : 2,
    }
 
    activities  = activity_service.filter(filters)

    print(activities)

    return HttpResponse(activities)
