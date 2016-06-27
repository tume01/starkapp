from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from services.BungalowService import BungalowService
from services.BungalowTypeService import BungalowTypeService
from services.HeadquarterService import HeadquarterService

from bungalow.models import Bungalow
from bungalow_type.models import BungalowType

@require_http_methods(['GET'])
def index(request):

    bungalows = BungalowService.getBungalows()

    paginator = Paginator(bungalows, 10)
    page = request.GET.get('page')

    try:
        pagineted_bungalows = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pagineted_bungalows = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pagineted_bungalows = paginator.page(paginator.num_pages)

    context = {
        'bungalows' : pagineted_bungalows,
        'bungalowTypes' : BungalowTypeService.getBungalowTypes(),
        'headquarters' : HeadquarterService().getHeadquarters(),
        'status_choices' : Bungalow.STATUS_CHOICES,        # Aun no se filtra por Status
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/bungalow/index.html', context)

@require_http_methods(['POST'])
def refresh_table(request):

    bungalow_type_id = int(request.POST['bungalow_type_id'])
    headquarter_id = int(request.POST['headquarter_id'])
    page = 1
    if 'page' in request.POST:
        page = int(request.POST['page'])
    
    print('#### >> ',bungalow_type_id,headquarter_id,page)

    bungalows = BungalowService.getBungalows()

    if (bungalow_type_id != -1):
        print("Filter by Type_ID")
        bungalows = bungalows.filter(bungalow_type_id = bungalow_type_id)

    if (headquarter_id != -1):
        print("Filter by Headquarter_ID")
        bungalows = bungalows.filter(headquarter_id = headquarter_id)

    paginator = Paginator(bungalows, 10)
    pagineted_bungalows = paginator.page(page)

    context = {
        'bungalows' : pagineted_bungalows
    }

    return render_to_response('Admin/bungalow/index_table.html', context)


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo',
        'status_choices' : Bungalow.STATUS_CHOICES,
        'bungalowTypes' : BungalowTypeService.getBungalowTypes(),
        'headquarters' : HeadquarterService().getHeadquarters(),
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

    bungalowTypeId = int(request.POST['bungalow_type_id'])
    insert_data["bungalow_type_id"] = bungalowTypeId

    headquarterId = int(request.POST['headquarter_id'])
    insert_data["headquarter_id"] = headquarterId

    BungalowService.create(insert_data)

    return HttpResponseRedirect(reverse('bungalow:index'))

@require_http_methods(['GET'])
def update_index(request, bungalow_id):

    bungalow = BungalowService.findBungalow(bungalow_id)

    context = {
        'titulo' : 'titulo',
        'bungalow' : bungalow,
        'bungalowTypes' : BungalowTypeService.getBungalowTypes(),
        'headquarters' : HeadquarterService().getHeadquarters(),
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
