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
        'titulo': 'tittle'
    }

    return render(request, 'Admin/Activities/index_activity.html', context)

@require_http_methods(['POST'])
def create_activity(request):
    
    form = ActivityForm(request.POST)

    context = {
        'titulo': 'titulo'
    }

    if validateForm(form, request):

        price = form.cleaned_data['price']
        attendance = form.cleaned_data['attendance']
        start_date = form.cleaned_data['start_date']
        end_date   = form.cleaned_data['end_date']

        return render(request, 'Admin/Activities/new_activity.html', context)

    else:

        return HttpResponseRedirect(reverse('activities:index'))

        
def validateForm(form, request):

    if form.is_valid():

        errors = form.errors.as_data()

        for error in errors:

            validation_instance = errors[error]

            for instance_error in validation_instance:

                for error_message in instance_error:

                    messages.error(request, (error_message))
    
        return request                    

    return False

@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo': 'tittle'
    }

    return render(request, 'Admin/Activities/new_activity.html', context)

@require_http_methods(['POST'])
def delete(request):
    
    activity_id = request.POST['id']

    activity_service = ActivityService()

    activity = activity_service.delete(activity_id)

    return HttpResponseRedirect(reverse('activities:index'))


@require_http_methods(['GET'])
def update_index(request):

    activity_service = ActivityService()
    
    activity_id = request.GET['id']

    activity  = activity_service.find(activity_id)

    context = {
        'titulo': 'tittle',
        'activity': activity
    }

    return render(request, 'Admin/Activities/edit_activity.html', context)

@require_http_methods(['POST'])
def update(request):

    activity_id = request.POST['id']

    activity_service = ActivityService()

    activity = activity_service.update(activity_id, update_data)

    return HttpResponseRedirect(reverse('activities:index'))

