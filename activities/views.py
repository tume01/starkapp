from datetime import datetime
from .forms import ActivityForm
import json
from django.template import loader
from services.EnvironmentService import EnvironmentService
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Adapters.FormValidator import FormValidator
from services.ActivityService import ActivityService
from services.ActivityTypeService import ActivityTypeService
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@require_http_methods(['GET'])
def index(request):

    activity_service = ActivityService()

    filters = getActivityFilters(request)

    activities = activity_service.filter(filters)

    activity_types = ActivityTypeService.getActivityTypes()
    
    paginator = Paginator(activities, 10)

    page = request.GET.get('page')

    try:
        activities = paginator.page(page)

    except PageNotAnInteger:
        activities = paginator.page(1)

    except EmptyPage:
        activities = paginator.page(paginator.num_pages)

    context = {
        'titulo': 'tittle',
        'activities': activities,
        'activity_types': activity_types
    }

    return render(request, 'Admin/Activities/index_activity.html', context)

def getActivityFilters(request):

    filters = {}

    filters['status'] = None;

    if request.GET.get('name'):
        filters['name__contains'] = request.GET.get('name')

    if request.GET.get('activity_type_id'):
        filters['activity_type_id'] = request.GET.get('activity_type_id')

    if request.GET.get('start_date'):
        start_date = datetime.strptime(request.GET.get('start_date'), "%m/%d/%Y")

        filters['start_date__gte'] = start_date

    if request.GET.get('end_date'):
        end_date = datetime.strptime(request.GET.get('end_date'), "%m/%d/%Y")

        filters['end_date__lte'] = end_date

    if request.GET.get('attendance'):
        filters['attendance'] = request.GET.get('attendance')

    return filters

@require_http_methods(['POST'])
def create_activity(request):

    form = ActivityForm(request.POST)

    context = {
        'titulo': 'titulo'
    }

    request = FormValidator.validateForm(form, request)

    if not request:

        activity_service = ActivityService()
        activity_types_service = ActivityTypeService()
        environments_service = EnvironmentService()

        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        attendance = form.cleaned_data['attendance']
        start_date = form.cleaned_data['start_date']
        end_date   = form.cleaned_data['end_date']
        activity_type_id = form.cleaned_data['activity_type']
        enviroment_id = form.cleaned_data['environments']

        enviroment = environments_service.getEnviromentById(enviroment_id)
        activity_type = activity_types_service.getActivityType(activity_type_id)

        insert_data = {
            'name': name,
            'price': price,
            'attendance': attendance,
            'start_date': start_date,
            'end_date': end_date,
            'activity_type': activity_type,
            'enviroment': enviroment
        }

        activity_service.create(insert_data)

        return HttpResponseRedirect(reverse('activities:index'))

    else:

        return render(request, 'Admin/Activities/new_activity.html', context)

@require_http_methods(['GET'])
def create_index(request):

    activity_types_service = ActivityTypeService()
    environments_service = EnvironmentService()

    activity_types = activity_types_service.getActivityTypes()
    environments = environments_service.getEnvironment()

    context = {
        'titulo': 'tittle',
        'activity_types': activity_types,
        'environments': environments,
    }

    return render(request, 'Admin/Activities/new_activity.html', context)

@require_http_methods(['GET'])
def delete(request, activity_id):

    activity_service = ActivityService()

    activity = activity_service.update(activity_id, {'status': datetime.now()})

    return HttpResponseRedirect(reverse('activities:index'))


@require_http_methods(['GET'])
def update_index(request, activity_id):

    activity_service = ActivityService()
    activity_types_service = ActivityTypeService()
    environments_service = EnvironmentService()

    activity  = activity_service.getActivity(activity_id)
    activity_types = activity_types_service.getActivityTypes()
    environments = environments_service.getEnvironment()

    context = {
        'titulo': 'tittle',
        'activity': activity,
        'activity_types': activity_types,
        'environments': environments
    }

    return render(request, 'Admin/Activities/edit_activity.html', context)

@require_http_methods(['POST'])
def update(request, activity_id):

    form = ActivityForm(request.POST)

    if FormValidator.validateForm(form, request):
        context = {
            'titutlo': 'titulo'
        }
        return HttpResponseRedirect(reverse('activities:select', args=[activity_id]))

    else:
        activity_service = ActivityService()
        environments_service = EnvironmentService()
        activity_types_service = ActivityTypeService()

        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        end_date = form.cleaned_data['end_date']
        start_date = form.cleaned_data['start_date']
        attendance = form.cleaned_data['attendance']
        enviroment_id = form.cleaned_data['environments']
        activity_type_id = form.cleaned_data['activity_type']

        enviroment = environments_service.getEnviromentById(enviroment_id)
        activity_type = activity_types_service.getActivityType(activity_type_id)

        update_data = {
            'name': name,
            'price': price,
            'end_date': end_date,
            'attendance': attendance,
            'start_date': start_date,
            'activity_type': activity_type,
            'enviroment': enviroment
        }

        activity_service.update(activity_id, update_data)

        return HttpResponseRedirect(reverse('activities:index'))

def index_course(request):

    activity_service = ActivityService()

    filters = getActivityFilters(request)

    filters['activity_type_id'] = 2

    activities = activity_service.filter(filters)

    paginator = Paginator(activities, 10)

    page = request.GET.get('page')

    try:
        activities = paginator.page(page)

    except PageNotAnInteger:
        activities = paginator.page(1)

    except EmptyPage:
        activities = paginator.page(paginator.num_pages)

    context = {
        'titulo': 'tittle',
        'activities': activities
    }

    return render(request, 'Admin/Activities/index_course.html', context)
