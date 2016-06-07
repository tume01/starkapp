from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from services.BungalowService import BungalowService
from services.BungalowTypeService import BungalowTypeService

from bungalow.models import Bungalow
from bungalow_type.models import BungalowType

@require_http_methods(['GET'])
def index(request):

    bungalows = BungalowService.getBungalows()

    context = {
        'bungalows' : bungalows,
        'bungalowTypes' : BungalowTypeService.getBungalowTypes(),
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/bungalow/index.html', context)

@require_http_methods(['POST'])
def index_filters(request):

    from django.core import serializers

    bungalow_type_id = request.POST['bungalow_type_id']
    member_name = request.POST['member_name']
    headquarter_id = request.POST['headquarter_id']
    

    bungalows = BungalowService.getBungalows()


    if (bungalow_type_id != -1):
        bungalows = bungalows.filter(bungalow_type_id = bungalow_type_id)
    # if (headquarter_id != -1):
    #     bungalows = bungalows.filter(headquarter_id = headquarter_id)

    context = {
        'bungalows' : bungalows
    }

    return render_to_response('Admin/bungalow/index_table.html', context)


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo',
        'status_choices' : Bungalow.STATUS_CHOICES,
        'bungalowTypes' : BungalowTypeService.getBungalowTypes(),
    }
    a = Bungalow.STATUS_CHOICES

    for status in a:
        print("Status:",status[0], status[1])

    return render(request, 'Admin/bungalow/new_bungalow.html', context)


@require_http_methods(['POST'])
def create_bungalow(request):

    insert_data = {}

    insert_data["number"] = request.POST['number']
    insert_data["location"] = request.POST['location']
    insert_data["status"] = request.POST['status']

    bungalowTypeId = request.POST['bungalow_type_id']
    insert_data["bungalow_type"] = BungalowTypeService.findBungalowType(bungalowTypeId)

    BungalowService.create(insert_data)

    return HttpResponseRedirect(reverse('bungalow:index'))


# def validateForm(form, request):
#     if form.is_valid():
#         errors = form.errors.as_data()

#         for error in errors:
#             validation_instance = errors[error]
#             for instance_error in validation_instance:
#                 for error_message in instance_error:
#                     messages.error(request, (error_message))    
#         return request


@require_http_methods(['GET'])
def update_index(request, bungalow_id):

    bungalow = BungalowService.findBungalow(bungalow_id)

    context = {
        'titulo' : 'titulo',
        'bungalow' : bungalow,
        'bungalowTypes' : BungalowTypeService.getBungalowTypes(),
    }

    return render(request, 'Admin/bungalow/update_bungalow.html', context)

@require_http_methods(['POST'])
def update_bungalow(request, bungalow_id):

    bungalowTypeId = request.POST['bungalow_type_id']

    insert_data = {}
    insert_data["number"] = request.POST['number']
    insert_data["location"] = request.POST['location']
    insert_data["status"] = request.POST['status']
    insert_data["bungalow_type"] = BungalowTypeService.findBungalowType(bungalowTypeId)

    BungalowService.update(bungalow_id, insert_data)

    return HttpResponseRedirect(reverse('bungalow:index'))
