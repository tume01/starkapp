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
def list_promotion_event(request):

    promotion_service = PromotionsService()

    event_promotion_service = EventPromotionService()
    promotions = event_promotion_service.getEventPromotion()
    

    promotion_names=[]
    promotion_start=[]
    promotion_end=[]

    for promotion in promotions:
        promotion_super = promotion_service.getPromotion(promotion.promotion_id)
        promotion_names.append(promotion_super.description)
        promotion_start.append(promotion_super.startDate)
        promotion_end.append(promotion_super.endDate)

    promotions_all = zip(promotions,promotion_names,promotion_start,promotion_start)

    context = {
        'promotions' : promotions_all,
    }

    return render(request,'Admin/Promotions/list_promotion_event.html',context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
def list_promotion_bungalow(request):

    promotion_service = PromotionsService()

    bungalow_promotion_service = BungalowPromotionService()
    promotions = bungalow_promotion_service.getBungalowPromotion()
    
    promotion_names=[]
    promotion_start=[]
    promotion_end=[]

    for promotion in promotions:
        promotion_super = promotion_service.getPromotion(promotion.promotion_id)
        promotion_names.append(promotion_super.description)
        promotion_start.append(promotion_super.startDate)
        promotion_end.append(promotion_super.endDate)

    promotions_all = zip(promotions,promotion_names,promotion_start,promotion_start)

    context = {
        'promotions' : promotions_all,
    }

    return render(request,'Admin/Promotions/list_promotion_bungalow.html',context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
def list_promotion_membership(request):

    promotion_service = PromotionsService()

    membership_promotion_service = MembershipPromotionService()
    promotions = membership_promotion_service.getMembershipPromotion()

    promotion_names=[]
    promotion_start=[]
    promotion_end=[]

    for promotion in promotions:
        
        promotion_super = promotion_service.getPromotion(promotion.promotion_id)
        promotion_names.append(promotion_super.description)
        promotion_start.append(promotion_super.startDate)
        promotion_end.append(promotion_super.endDate)

    promotions_all = zip(promotions,promotion_names,promotion_start,promotion_end)

    context = {
        'promotions' : promotions_all,
    }
    return render(request,'Admin/Promotions/list_promotion_membership.html',context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
def get_membership(request):

    membership_type_service = MembershipTypeService()

    membership_types = membership_type_service.getMembershipTypes()

    context= {
        'membership_types' : membership_types
    }

    return render_to_response('Admin/Promotions/membership_types_table.html',context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
def get_bungalows(request):

    bungalow_type_service = BungalowTypeService()

    bungalow_types = bungalow_type_service.getBungalowTypes()

    membership_type_service = MembershipTypeService()

    membership_types = membership_type_service.getMembershipTypes()

    context = {
        'bungalow_types' : bungalow_types,
        'membership_types' : membership_types
    }

    return render_to_response('Admin/Promotions/bungalow_types_table.html',context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
def get_events(request):

    event_types_services = EventsTypeService()

    event_types = event_types_services.getEventsType()

    membership_type_service = MembershipTypeService()

    membership_types = membership_type_service.getMembershipTypes()

    context = {
        'event_types' : event_types,
        'membership_types' : membership_types
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
def index_edit_promotion_membership(request):

    id_promotion = request.POST['id']

    promotion_service = PromotionsService()

    membership_promotion_service = MembershipPromotionService()

    promotion_super = promotion_service.getPromotion(id_promotion)

    promotion = membership_promotion_service.findMembershipPromotion(id_promotion)

    context = {
        'promotion' : promotion_super,
        'percentage': promotion.percentage,
        'membership_type_id' : promotion.membership_type_id
    }

    return render(request, 'Admin/Promotions/edit_promotion_membership.html', context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def index_edit_promotion_bungalow(request):

    id_promotion = request.POST['id']

    promotion_service = PromotionsService()

    promotion_super = promotion_service.getPromotion(id_promotion)

    bungalow_promotion_service = BungalowPromotionService()

    promotion = bungalow_promotion_service.getBungalowPromotion(id_promotion)

    context = {
        'promotion' : promotion_super,
        'percentage': promotion.percentage,
        'membership_type_id' : promotion.membership_type_id
    }

    return render(request, 'Admin/Promotions/edit_promotion_bungalow.html', context)

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def index_edit_promotion_event(request):

    id_promotion = request.POST['id']

    promotion_service = PromotionsService()

    promotion_super = promotion_service.getPromotion(id_promotion)

    event_promotion_service = EventPromotionService()

    promotion = bungalow_promotion_service.getEventPromotion(id_promotion)

    context = {
        'promotion' : promotion_super,
        'percentage': promotion.percentage,
        'membership_type_id' : promotion.membership_type_id
    }

    return render(request, 'Admin/Promotions/edit_promotion_event.html', context)


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

    promotion_service = PromotionsService()

    insert_data = {}

    promotion_start_date = datetime.datetime.strptime(request.POST.get("start_date"),"%m/%d/%Y %H:%M %p").date()
    
    promotion_end_date = datetime.datetime.strptime(request.POST.get("end_date"),"%m/%d/%Y %H:%M %p").date()

    insert_data["description"] = request.POST.get('description')

    insert_data["startDate"] = promotion_start_date

    insert_data["endDate"] = promotion_end_date

    insert_data["status"] = 1

    promotion = promotion_service.create(insert_data)

    promotion_id = promotion.id

    #INTERMEDIATE TABLE MEMBERSHIP AND PROMOTION

    membership_percentage_array = request.POST.getlist('membership_percentage')

    membership_id_array = request.POST.getlist('membership_type')
    

    #INTERMEDIATE TABLE BUNGALOW, MEMBERSHIP AND PROMOTION

    insert_bungalow_promotion = {}

    bungalow_percentage_array = request.POST.getlist('bungalow_percentage')

    bungalow_id_array = request.POST.getlist('bungalow_type')

    membership_bungalow_id_array = request.POST.getlist('membership_bungalow_type')


    #INTERMEDIATE TABLE MEMBERSHIP, EVENT AND PROMOTION

    insert_event_promotion = {}

    event_percentage_array = request.POST.getlist('event_percentage')

    event_id_array = request.POST.getlist('event_type')

    membership_event_id_array = request.POST.getlist('membership_event_type')

    
    #Save promotions for membership
    if  membership_id_array:

        membership_promotion_service = MembershipPromotionService()
        insert_promotion_membership = {}
        
        for membership_id,percentage in zip(membership_id_array,membership_percentage_array):

            insert_promotion_membership['membership_type_id'] = membership_id
            insert_promotion_membership['percentage'] = percentage
            insert_promotion_membership['promotion_id'] = promotion_id

            membership_promotion_service.create(insert_promotion_membership)

        return HttpResponseRedirect(reverse('promotions:list_membership'))


    #Save promotions for bungalows
    if bungalow_id_array:

        bungalow_promotion_service = BungalowPromotionService()
        insert_promotion_bungalow = {}

        for bungalow_id,member_id,percentage in zip(bungalow_id_array,membership_bungalow_id_array,bungalow_percentage_array):

            insert_promotion_bungalow['membership_type_id'] = member_id
            insert_promotion_bungalow['bungalow_type_id'] = bungalow_id
            insert_promotion_bungalow['percentage'] = percentage
            insert_promotion_bungalow['promotion_id'] = promotion_id
            bungalow_promotion_service.create(insert_promotion_bungalow)

        return HttpResponseRedirect(reverse('promotions:list_bungalow'))

    #Save promotions for events
    if  event_id_array:

        event_promotion_service = EventPromotionService()
        insert_promotion_event = {}

        for event_id,member_id,percentage in zip(event_id_array,membership_event_id_array,bungalow_percentage_array):

            insert_promotion_event['membership_type_id'] = member_id
            insert_promotion_event['event_type_id'] = bungalow_id
            insert_promotion_event['percentage'] = percentage
            insert_promotion_event['promotion_id'] = promotion_id
            event_promotion_service.create(insert_promotion_event)

    return HttpResponseRedirect(reverse('promotions:list_event'))

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_promotion_membership(request):

    id_edit = request.POST['id']

    promotion_service = PromotionsService()

    edit_data = {}

    edit_data["description"] = request.POST.get('description')
    edit_data["startDate"] = datetime.datetime.strptime(request.POST.get("start_date"),"%m/%d/%Y %H:%M %p").date()
    edit_data["endDate"] = datetime.datetime.strptime(request.POST.get("end_date"),"%m/%d/%Y %H:%M %p").date()

    membership_id = int(request.POST.get('membership'))

    promotion_service.update(id_edit, edit_data)

    membership_promotion_service = MembershipPromotionService()

    promotion = promotion_service.getPromotion(id_edit)

    promo_member =  promotion.membershippromotion_set.all()

    filters = {
        'promotion_id' : id_edit,
        'membership_type_id' : membership_id
    }

    promotions = membership_promotion_service.filter(filters)

    edit_data = {}

    edit_data["percentage"] = request.POST.get('percentage')

    for promotion in promotions:

        membership_promotion_service.update(promotion.id,edit_data)

    return HttpResponseRedirect(reverse('promotions:list_membership'))

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_promotion_bungalow(request):

    id_edit = request.POST['id']

    promotion_service = PromotionsService()

    edit_data = {}

    edit_data["description"] = request.POST.get('description')
    edit_data["startDate"] = datetime.datetime.strptime(request.POST.get("start_date"),"%m/%d/%Y %H:%M %p").date()
    edit_data["endDate"] = datetime.datetime.strptime(request.POST.get("end_date"),"%m/%d/%Y %H:%M %p").date()

    bungalow_promotion_service = BungalowPromotionService()

    membership_id = int(request.POST.get('membership'))

    filters = {
        'promotion_id' : id_edit,
        'membership_type_id' : membership_id
    }

    promotion = bungalow_promotion_service.filter(filters)
        
    edit_data = {}

    edit_data["percentage"] = request.POST.get('percentage')

    for promotion in promotions:

        bungalow_promotion_service.update(promotion.id, edit_data)

    return HttpResponseRedirect(reverse('promotions:list_bungalow'))

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def edit_promotion_event(request):

    id_edit = request.POST['id']

    promotion_service = PromotionsService()

    edit_data = {}

    edit_data["description"] = request.POST.get('description')
    edit_data["startDate"] = datetime.datetime.strptime(request.POST.get("start_date"),"%m/%d/%Y %H:%M %p").date()
    edit_data["endDate"] = datetime.datetime.strptime(request.POST.get("end_date"),"%m/%d/%Y %H:%M %p").date()

    event_promotion_service = EventPromotionService()

    membership_id = int(request.POST.get('membership'))

    filters = {
        'promotion_id' : id_edit,
        'membership_type_id' : membership_id
    }

    promotion = bungalow_promotion_service.filter(filters)

    edit_data = {}

    edit_data["percentage"] = request.POST.get('percentage')

    for promotion in promotions:

        promotion_service.update(promotion_id, edit_data)

    return HttpResponseRedirect(reverse('promotions:list_event'))
