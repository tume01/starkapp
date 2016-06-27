from .forms import PoliticForm
from adapters.FormValidator import FormValidator

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.PoliticsService import PoliticsService
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def index(request):

    politic_service = PoliticsService()

    politics = politic_service.getPolitics()

    context = {
        'politics' : politics,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Politics/index_politics.html', context) 


@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo',
    }

    return render(request, 'Admin/Politics/new_politic.html', context)

@require_http_methods(['POST'])
def create_politic(request):

    form = PoliticForm(request.POST)

    context = {
        'titulo': 'titulo'
    }

    request = FormValidator.validateForm(form, request)

    politic_service = PoliticsService()

    if not request:

        name = form.cleaned_data['name']
        value = form.cleaned_data['value']

        insert_data = {
            'name': name,
            'value': value,
        }

        politic_service.create(insert_data)

        return HttpResponseRedirect(reverse('politics:index'))

    else:

        return render(request, 'Admin/Politics/new_politic.html', context)

@require_http_methods(['GET'])
def update_index(request, politic_id):

    politic_service = PoliticsService()

    politic = politic_service.find(politic_id)

    context = {
        'titulo' : 'titulo',
        'politic' : politic
    }

    return render(request, 'Admin/Politics/edit_politic.html', context)

@require_http_methods(['POST'])
def update_politic(request, politic_id):

    form = PoliticForm(request.POST)

    politic_service = PoliticsService()

    politic = politic_service.find(politic_id)

    if FormValidator.validateForm(form, request):
        context = {
            'titulo': 'titulo',
            'politic' : politic
        }
        return render(request, 'Admin/Politics/edit_politic.html', context)

    else:
        
        name  = form.cleaned_data['name']
        value = form.cleaned_data['value']


        update_data = {
            'value': value,
            'name' : name
        }

        politic_service.update(politic_id, update_data)

        return HttpResponseRedirect(reverse('politics:index'))

@require_http_methods(['GET'])
def delete(request, politic_id):
    
    politic_service = PoliticsService()

    politic = politic_service.delete(politic_id)

    return HttpResponseRedirect(reverse('politics:index'))