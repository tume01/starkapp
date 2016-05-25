from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.PromotionsService import PromotionsService
from django.views.decorators.http import require_http_methods
from Adapters.FormValidator import FormValidator
from .forms import PromotionForm


@require_http_methods(['GET'])
def index(request):

    promotion_service = PromotionsService()

    promotions = promotion_service.getPromotions()

    context = {
        'promotions' : promotions,
    }

    return render(request, 'Admin/Promotions/index_promotion.html', context) 


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Promotions/new_promotion.html', context)

@require_http_methods(['POST'])
def edit_index(request):

    id_promotion = request.POST['id']

    promotion_service = PromotionsService()

    promotion = promotion_service.getPromotion(id_promotion)

    context = {
        'promotion' : promotion,
    }

    return render(request, 'Admin/Promotions/edit_promotion.html', context)

@require_http_methods(['POST'])
def delete_promotion(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    promotion_service = PromotionsService()

    promotion_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('promotions:index'))


@require_http_methods(['POST'])
def create_promotion(request):

    form = PromotionForm(request.POST)

    request = FormValidator.validateForm(form, request)

    if not request:

        insert_data = {}

        insert_data["description"] = form.cleaned_data['description']

        insert_data["percentage"] = form.cleaned_data['percentage']

        insert_data["status"] = 1

        promotion_service = PromotionsService()

        promotion_service.create(insert_data)

        return HttpResponseRedirect(reverse('promotions:index'))

    else:
        context = {
            'titulo' : 'titulo'
        }

        return render(request, 'Admin/Promotions/new_promotion.html', context)


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
