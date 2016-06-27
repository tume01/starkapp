
from django.shortcuts import render, render_to_response
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from services.BungalowTypeService import BungalowTypeService
from services.HeadquarterService import HeadquarterService
from services.BungalowRaffleService import BungalowRaffleService
from services.BungalowService import BungalowService
import datetime


# Create your views here.

@require_http_methods(['GET'])
def admin_index(request):
    raffles = BungalowRaffleService.getRaffles()

    paginator = Paginator(raffles, 10)
    page = request.GET.get('page')

    try:
        paginated_raffless = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_raffless = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_raffless = paginator.page(paginator.num_pages)

    context = {
        'raffles': paginated_raffless,
        'bungalowTypes': BungalowTypeService.getBungalowTypes(),
        'headquarters': HeadquarterService().getHeadquarters(),
        'titulo': 'titulo'
    }

    return render(request, 'Admin/bungalowRaffle/index.html', context)
    pass


@require_http_methods(['POST'])
def admin_refresh_table(request):
    # bungalow_type_id = int(request.POST['bungalow_type_id'])
    headquarter_id = int(request.POST['headquarter_id'])
    # status = int(request.POST['status'])

    page = 1
    if 'page' in request.POST:
        page = int(request.POST['page'])

    raffles = BungalowRaffleService.getRaffles()
    #
    # if (status != -1):
    #     print("Filter by Status")
    #     reservations = raffles.filter(status=status)

    if (headquarter_id != -1):
        print("Filter by Headquarter")
        raffles = raffles.filter(bungalow_headquarter_id=headquarter_id)

    paginator = Paginator(raffles, 10)
    paginated_raffless = paginator.page(page)

    context = {
        'raffles': paginated_raffless,
    }

    return render_to_response('Admin/bungalowRaffle/index_table.html', context)


@require_http_methods(['GET'])
def admin_create_index(request):
    context = {
        'bungalows': BungalowService.getBungalows(),
        'titulo': 'titulo'
    }
    return render(request, 'Admin/bungalowRaffle/create_raffle.html', context)


@require_http_methods(['POST'])
def admin_create(request):
    bungalow = BungalowService.findBungalow(request.POST['bungalow_id'])
    member = getRandomMember()
    arrival_date = datetime.datetime.strptime(request.POST['arrival_date'], '%d/%m/%Y')
    create_new_raffle(bungalow, member, arrival_date)

    email = EmailMessage('Sorteo de Bungalow' ,
                             'Hola ' + member.name + ',\n\nHas sido seleccionado por sorteo y has ganado la estadia en el bungalow'+
                         bungalow.number + ' en la sede ' + bungalow.headquarter.name + '.',
                             to=[member.email])

    email.send()
    return HttpResponseRedirect(reverse('bungalowRaffle:admin_index'))


# Helpers
def create_new_raffle(bungalow, member, arrival_date):
    insert_data = {}

    insert_data["bungalow_id"] = bungalow.id
    insert_data["bungalow_number"] = bungalow.number
    insert_data["bungalow_type_id"] = bungalow.bungalow_type.id
    insert_data["bungalow_type_name"] = bungalow.bungalow_type.name
    insert_data["bungalow_headquarter_id"] = bungalow.headquarter.id
    insert_data["bungalow_headquarter_name"] = bungalow.headquarter.name

    insert_data["member_id"] = member.id
    insert_data["member_name"] = member.name
    insert_data["member_membership_name"] = member.membership.membership_type.name
    insert_data["member_paternalLastName"] = member.paternalLastName
    insert_data["member_maternalLastName"] = member.maternalLastName

    insert_data["arrival_date"] = arrival_date

    return BungalowRaffleService.create(insert_data)


import random
from members.models import Member


def getRandomMember():
    members = Member.objects.all()
    member = random.choice(members)
    return member
