from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from services.BungalowsService import BungalowsService

bungalow_service = BungalowsService()



@require_http_methods(['GET'])
def index(request):
    bungalow_list = bungalow_service.getBungalows()
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

    return render(request, 'Admin/Bungalows/new_bungalow.html', context)

@require_http_methods(['POST'])
def create_bungalow(request):

    insert_data = {}

    insert_data["number"] = request.POST['number']

    insert_data["location"] = request.POST['location']

    insert_data["status"] = request.POST['status']

    insert_data["bungalow_type_id"] = 1

    bungalow_service = BungalowsService()

    bungalow_service.create(insert_data)

    return HttpResponseRedirect(reverse('bungalows:index'))
