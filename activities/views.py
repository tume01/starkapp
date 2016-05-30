from datetime import datetime
from .forms import ActivityForm
import json
from django.template import loader
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from adapters.FormValidator import FormValidator
from services.ActivityService import ActivityService
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@require_http_methods(['GET'])
def index(request):

    activity_service = ActivityService()

    filters = getActivityFilters(request)

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

    return render(request, 'Admin/Activities/index_activity.html', context)

def getActivityFilters(request):


    filters = {}

    if request.GET.get('name'):
        filters['name'] = request.GET.get('name')

    if request.GET.get('price'):
        filters['price'] = request.GET.get('price')

    if request.GET.get('start_date'):
        start_date = datetime.strptime(request.GET.get('start_date'), "%m/%d/%Y")

        filters['start_date__gte'] = start_date

    if request.GET.get('end_date'):
        end_date = datetime.strptime(request.GET.get('end_date'), "%m/%d/%Y")

        filters['end_date__lte'] = end_date

    if request.GET.get('attendance'):
        filters['attendance'] = request.GET.get('end_date')

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

        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        attendance = form.cleaned_data['attendance']
        start_date = form.cleaned_data['start_date']
        end_date   = form.cleaned_data['end_date']

        insert_data = {
            'name': name,
            'price': price,
            'attendance': attendance,
            'start_date': start_date,
            'end_date': end_date
        }

        activity_service.create(insert_data)

        return HttpResponseRedirect(reverse('activities:index'))

    else:

        return render(request, 'Admin/Activities/new_activity.html', context)

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
def update_index(request, activity_id):

    activity_service = ActivityService()

    activity  = activity_service.getActivity(activity_id)

    context = {
        'titulo': 'tittle',
        'activity': activity
    }

    return render(request, 'Admin/Activities/edit_activity.html', context)

@require_http_methods(['POST'])
def update(request, activity_id):

    activity_id = request.GET.get('activity_id')


    form = ActivityForm(request.POST)

    activity_service = ActivityService()

    if FormValidator.validateForm(form, request):
        context = {
            'titutlo': 'titulo'
        }
        return render(request, 'Admin/Activities/new_activity.html', context)

    else:
        activity_service = ActivityService()

        price = form.cleaned_data['price']
        attendance = form.cleaned_data['attendance']
        start_date = form.cleaned_data['start_date']
        end_date   = form.cleaned_data['end_date']

        update_date = {
            'price': price,
            'attendance': attendance,
            'start_date': start_date,
            'end_date': end_date
        }

        activity_service.update(activity_id, update_date)

        return HttpResponseRedirect(reverse('activities:index'))

    activity = activity_service.update(activity_id, update_data)

    return HttpResponseRedirect(reverse('activities:index'))

