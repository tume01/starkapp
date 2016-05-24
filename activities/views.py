from datetime import datetime
from .forms import ActivityForm
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

    activities = ActivityService()

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

@require_http_methods(['POST'])
def create_activity(request):

    form = ActivityForm(request.POST)

    context = {
        'titulo': 'titulo'
    }

    request = FormValidator.validateForm(form, request)
    if not request:

        activity_service = ActivityService()

        price = form.cleaned_data['price']
        attendance = form.cleaned_data['attendance']
        start_date = form.cleaned_data['start_date']
        end_date   = form.cleaned_data['end_date']

        insert_data = {
            'price': price,
            'attendance': attendance,
            'start_date': start_date,
            'end_date': end_date
        }

        activity_service.create(insert_data)

        return HttpResponseRedirect(reverse('activities:index'))

    else:

        return render(request, 'Admin/Activities/new_activity.html', context)


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

    activity_id = request.GET.get('id')

    activity  = activity_service.find(activity_id)

    context = {
        'titulo': 'tittle',
        'activity': activity
    }

    return render(request, 'Admin/Activities/edit_activity.html', context)

@require_http_methods(['POST'])
def update(request):

    activity_id = request.POST['id']


    form = ActivityForm(request.POST)

    activity_service = ActivityService()

    if FormValidator.validateForm(form, request):

        return render(request, 'Admin/Activities/new_activity.html', context)

    else:
        activity_service = ActivityService()

        price = form.cleaned_data['price']
        attendance = form.cleaned_data['attendance']
        start_date = form.cleaned_data['start_date']
        end_date   = form.cleaned_data['end_date']

        insert_data = {
            'price': price,
            'attendance': attendance,
            'start_date': start_date,
            'end_date': end_date
        }

        activity_service.create(insert_data)

        return HttpResponseRedirect(reverse('activities:index'))

    activity = activity_service.update(activity_id, update_data)

    return HttpResponseRedirect(reverse('activities:index'))

