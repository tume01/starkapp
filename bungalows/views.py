from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from services.BungalowService import BungalowService
from services.BungalowTypeService import BungalowTypeService

from bungalows.models import *

@require_http_methods(['GET'])
def index(request):
    bungalow_list = BungalowService.getBungalows()
    paginator = Paginator(bungalow_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')

    try:
        bungalows = paginator.page(page)
    except PageNotAnInteger:
        bungalows = paginator.page(1)
    except EmptyPage:
        bungalows = paginator.page(paginator.num_pages)

    context = {
        'bungalows' : bungalows,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Bungalows/index_bungalow.html', context)


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }
    print("ESTOY AQUI")
    return render(request, 'Admin/Bungalows/new_bungalow.html', context)


@require_http_methods(['POST'])
def create_bungalow(request):

    # form = BungalowForm(request.POST)
    
    # if validateForm(form, request):

    #     bungalow_type_id = form.cleaned_data['bungalow_type_id']
    #     status = form.cleaned_data['status']
    #     start_date = form.cleaned_data['start_date']
    #     end_date   = form.cleaned_data['end_date']

    #     return render(request, 'Admin/Bungalows/new_bungalow.html', context)

    # else:

    insert_data = {}

    insert_data["number"] = request.POST['number']
    insert_data["location"] = request.POST['location']
    insert_data["status"] = request.POST['status']

    # bungalowTypeId = request.POST['bungalow_type_id']
    # A la espera de que el front pase este parametro. Suerte Carlo
    bungalowTypeId = 34
    insert_data["bungalow_type"] = BungalowTypeService.findBungalowType(bungalowTypeId)

    BungalowService.create(insert_data)

    return HttpResponseRedirect(reverse('bungalows:index'))


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
        'bungalow' : bungalow
    }
    print("ESTOY AQUI")
    return render(request, 'Admin/Bungalows/update_bungalow.html', context)

@require_http_methods(['POST'])
def update_bungalow(request, bungalow_id):

    insert_data = {}
    insert_data["number"] = request.POST['number']
    insert_data["location"] = request.POST['location']
    insert_data["status"] = request.POST['status']

    # bungalowTypeId = request.POST['bungalow_type_id']
    # A la espera de que el front pase este parametro. Suerte Carlo
    bungalowTypeId = 34
    insert_data["bungalow_type"] = BungalowTypeService.findBungalowType(bungalowTypeId)

    BungalowService.update(bungalow_id, insert_data)

    return HttpResponseRedirect(reverse('bungalows:index'))