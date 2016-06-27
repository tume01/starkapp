from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.PromotionsService import PromotionsService
from django.views.decorators.http import require_http_methods
from adapters.FormValidator import FormValidator
from .forms import PromotionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core import serializers


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def index(request):

    promotion_service = PromotionsService()

    promotions = promotion_service.getPromotions()

    context = {
        'promotions' : promotions,
    }

    if request.session.has_key('promotion_inserted'):

        context.update({'promotion_inserted':request.session.get('promotion_inserted')})

        del request.session['promotion_inserted']

    elif request.session.has_key('promotion_deleted'):

        context.update({'promotion_deleted':request.session.get('promotion_deleted')})

        del request.session['promotion_deleted']

    elif request.session.has_key('promotion_edited'):

        context.update({'promotion_edited':request.session.get('promotion_edited')})

        del request.session['promotion_edited']

    return render(request, 'Admin/Promotions/index_promotion.html', context) 


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

    context = {
        'titulo' : 'titulo'
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

    request.session['promotion_deleted'] = "True"

    return HttpResponseRedirect(reverse('promotions:index'))



@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def create_promotion(request):

    form = PromotionForm(request.POST)

    request2 = FormValidator.validateForm(form, request)

    if not request2:

        insert_data = {}

        insert_data["description"] = form.cleaned_data['description']

        insert_data["percentage"] = form.cleaned_data['percentage']

        insert_data["status"] = 1

        promotion_service = PromotionsService()

        promotion_service.create(insert_data)

        request.session['promotion_inserted'] = "True"

        return HttpResponseRedirect(reverse('promotions:index'))

    else:
        context = {
            'titulo' : 'titulo'
        }

        return render(request, 'Admin/Promotions/new_promotion.html', context)



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

        request.session['promotion_edited'] = "True"
        
        promotion_service.update(id_edit, edit_data)

        return HttpResponseRedirect(reverse('promotions:index'))
