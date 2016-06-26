from django.template import loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.PromotionsService import PromotionsService
from services.MembershipTypeService import MembershipTypeService
from services.BungalowTypeService import BungalowTypeService
from services.EventsTypeService import EventsTypeService
from services.EventPromotionService import EventPromotionService
from services.BungalowPromotionService import BungalowPromotionService
from services.MembershipPromotionService import MembershipPromotionService
from django.views.decorators.http import require_http_methods
from adapters.FormValidator import FormValidator
from .forms import PromotionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core import serializers
import json
import datetime

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def index(request):

    promotion_service = PromotionsService()

    promotions = promotion_service.getPromotions()

    context = {
        'promotions' : promotions,
    }

    return render(request, 'Admin/Promotions/index_promotion.html', context) 

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
def get_bungalows(request):

    bungalow_type_service = BungalowTypeService()

    bungalow_types = bungalow_type_service.getBungalowTypes()

    context = {
        'bungalow_types' : bungalow_types
    }

    return render_to_response('Admin/Promotions/bungalow_types_table.html',context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
def get_events(request):

    event_types_services = EventsTypeService()

    event_types = event_types_services.getEventsType()

    context = {
        'event_types' : event_types
    }

    return render_to_response('Admin/Promotions/event_types_table.html',context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def filter(request):

    promotion_service = PromotionsService()

    filter_promotions = {}

    promStatus = request.POST['status']

    fromNum = request.POST['from_num']

    toNum = request.POST['to_num']

    if promStatus != '3':
        filter_promotions["status"] = promStatus

    if fromNum != '':
        filter_promotions["percentage__gte"] = fromNum

    if toNum != '':
        filter_promotions["percentage__lte"] = toNum

    promotions = promotion_service.filter(filter_promotions)

    data = serializers.serialize("json", promotions)

    return HttpResponse(data, content_type='application/json')



@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def create_index(request):

    membership_type_service = MembershipTypeService()
    membership_types = membership_type_service.getMembershipTypes()

    context = {
        'titulo' : 'titulo',
        'membership_types' : membership_types,
    }

    return render(request, 'Admin/Promotions/new_promotion.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_index(request):

    id_promotion = request.POST['id']

    promotion_service = PromotionsService()

    promotion = promotion_service.getPromotion(id_promotion)

    context = {
        'promotion' : promotion,
    }

    return render(request, 'Admin/Promotions/edit_promotion.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def delete_promotion(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    promotion_service = PromotionsService()

    promotion_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('promotions:index'))



@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def create_promotion(request):

    insert_data = {}

    insert_data["description"] = request.POST.get('description')

    insert_data["percentage"] = request.POST.get('percentage')

    insert_data["status"] = 1

    promotion_service = PromotionsService()

    promotion = promotion_service.create(insert_data)

    insert_promotion_relation = {}

    insert_promotion_relation["startDate"] = datetime.datetime.strptime(request.POST.get("start_date"),"%m/%d/%Y %H:%M %p").date()

    insert_promotion_relation["endDate"] = datetime.datetime.strptime(request.POST.get("end_date"),"%m/%d/%Y %H:%M %p").date()

    insert_promotion_relation["percentage"] = request.POST.get("percentage")

    insert_promotion_relation["promotion_id"] = promotion.id

    insert_promotion_relation["membership_type_id"] = request.POST.get('membership_type')
    
    promotion_selected = request.POST.get('promotion')

    if promotion_selected == "membership" :
        membership_promotion_service = MembershipPromotionService()
        membership_promotion_service.create(insert_promotion_relation)
        #servicio solo membership

    elif promotion_selected == "bungalow":
        insert_promotion_relation["bungalow_type_id"] = request.POST.get('bungalow_type')
        bungalow_promotion_service = BungalowPromotionService()
        bungalow_promotion_service.create(insert_promotion_relation)

        #servicio para bungalow
    else:
        insert_promotion_relation["event_type_id"] = request.POST.get('event_type')
        event_promotion_service = EventPromotionService()
        event_promotion_service.create(insert_promotion_relation)
        #servicio para eventos

    return HttpResponseRedirect(reverse('promotions:index'))


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_promotion(request):

    form = PromotionForm(request.POST)

    id_edit = request.POST['id']

    promotion_service = PromotionsService()

    if FormValidator.validateForm(form, request):

        promotion = promotion_service.getPromotion(id_edit)

        context = {
            'promotion' : promotion
        }

        return render(request, 'Admin/Promotions/edit_promotion.html', context)

    else:

        edit_data = {}

        edit_data["description"] = form.cleaned_data['description']

        edit_data["percentage"] = form.cleaned_data['percentage']
        
        promotion_service.update(id_edit, edit_data)

        return HttpResponseRedirect(reverse('promotions:index'))
