from datetime import datetime,timedelta
from .forms import ActivityForm
import json
from django.template import loader
from services.EnvironmentService import EnvironmentService 
from services.MemberService import MembersService
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from adapters.FormValidator import FormValidator
from services.ActivityService import ActivityService
from services.ActivityTypeService import ActivityTypeService
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings

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

    filters['deleted_at'] = None;

    if request.GET.get('name'):
        filters['name__contains'] = request.GET.get('name')

    if request.GET.get('activity_type_id'):
        filters['activity_type_id'] = request.GET.get('activity_type_id')

    if request.GET.get('start_date'):
        start_date = datetime.strptime(request.GET.get('start_date'), "%d/%m/%Y")

        filters['start_date__gte'] = start_date

    if request.GET.get('end_date'):
        end_date = datetime.strptime(request.GET.get('end_date'), "%d/%m/%Y")
        end_date = end_date + timedelta(hours=24)

        filters['end_date__lt'] = end_date

    if request.GET.get('attendance'):
        filters['attendance'] = request.GET.get('attendance')

    return filters

@require_http_methods(['POST'])
def create_activity(request):

    form = ActivityForm(request.POST, request.FILES)

    context = {
        'titulo': 'titulo'
    }

    photo = request.FILES['photo']

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
            'enviroment': enviroment,
            'photo': photo
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

    activity = activity_service.update(activity_id, {'deleted_at': datetime.now()})

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

def index_members(request, activity_id):

    activity_service = ActivityService()

    registrations = activity_service.getActivityMembers(activity_id)

    context = {
        'activity_id' : activity_id,
        'registrations' : registrations
    }

    return render(request, 'Admin/Activities/index_members.html', context)

def remove_member(request, activity_id, member_id):

    activity_service = ActivityService()

    if activity_service.removeMember(activity_id, member_id):
        messages.success(request, 'Miembro retirado de actvidad exitosamente')
        return HttpResponseRedirect(reverse('activities:members', args=[activity_id]))

    messages.error(request, 'Error al remover miembro')
    return HttpResponseRedirect(reverse('activities:members', args=[activity_id]))

def index_add_member(request, activity_id):
    
    members_service = MembersService()

    members = members_service.getMembers()

    context = {
        'members' : members,
        'activity_id' : activity_id
    }

    return render(request, 'Admin/Activities/add_member.html', context)

def add_member(request, activity_id):

    member_id = request.POST.get('member')

    activity_service = ActivityService()
    members_service = MembersService()

    member = members_service.getMember(member_id)

    if activity_service.addMember(activity_id, member):
        messages.success(request, 'Miembro ananido correctamente')
        return HttpResponseRedirect(reverse('activities:members', args=[activity_id]))
    
    messages.error(request, 'Error al anadir miembro')
    return HttpResponseRedirect(reverse('activities:add_member', args=[activity_id]))

def index_signUp(request):

    activity_service = ActivityService()

    activities = activity_service.getActivities()
    image_url = settings.MEDIA_URL

    context = {
        'activities' : activities,
        'image_url': image_url
    }

    return render(request, 'User/Activities/index.html', context)

@require_http_methods(['GET'])
def select_signUp(request, activity_id):
    
    activity_service = ActivityService()

    activity = activity_service.getActivity(activity_id)
    image_url = settings.MEDIA_URL

    context = {
        'activity' : activity,
        'image_url': image_url
    }

    return render(request, 'User/Activities/select.html', context)

@require_http_methods(['POST'])
def signup(request, activity_id):
    
    activity_service = ActivityService()
    members_service = MembersService()

    member = members_service.filter({'user_id':request.user.id}).first()

    if activity_service.addMember(activity_id, member):
        messages.success(request, 'Registro en Actividad exitoso')
        return HttpResponseRedirect(reverse('activities:user_activities'))
    
    messages.error(request, 'No se ha podido registrar en la activdad')
    return HttpResponseRedirect(reverse('activities:select_signup', args=[activity_id]))

def signout(request, activity_id):
    
    activity_service = ActivityService()
    members_service = MembersService()

    member = members_service.filter({'user_id':request.user.id}).first()

    if activity_service.removeMember(activity_id, member.id):
        messages.success(request, 'Miembro retirado de actvidad exitosamente')
        return HttpResponseRedirect(reverse('activities:user_activities'))

    messages.error(request, 'Error al remover miembro')
    return HttpResponseRedirect(reverse('activities:user_activities'))

def user_activities(request):
    
    members_service = MembersService()

    member = members_service.filter({'user_id':request.user.id}).first() 

    activities = member.activityregistration_set.filter(deleted_at=None)
    
    context = {
        'activities' : activities
    }

    return render(request, 'User/Activities/user_activities.html', context)

def getUsers(request):

    json_request = json.loads( request.body.decode('utf-8') )

    

    members_service = MembersService()

    #members = members_service.filter({'identity_document_type_id': document_type, 'document_number': document_number})

    return HttpResponse('hola')