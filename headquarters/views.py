from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from HeadquarterService import HeadquarterService

from adapters.FormValidator import FormValidator
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import HeadquarterForm

# Create your views here.

@require_http_methods(['GET'])
def index(request):
	headquarter_service = HeadquarterService()

def create_headquarters(request):
	request = FormValidator.validateForm(form, request)

	if not request:
		name = form.cleaned_data['name']
		location = form.cleaned_data['location']

		insert_data = {
			'name': name,
			'location': location,
		}

		headquarter_service.create(insert_data)

		return HttpResponseRedirect(reverse('TBD'))
	else
		return render(request, 'TBD', context)

@require_http_methods(['POST'])	
def update(request, headquearter_id):
	headquearter_id = request.GET.get('headquarter_id')

	form = HeadquarterForm(request.POST)
	headquarter_service = HeadquarterService()

	if FormValidator.validateForm(form, request):
		context = {
			'titulo': 'titulo'
		}
		return render(request, 'TBD', context)
	else:
		headquarter_service = HeadquarterService()

		name = form.cleaned_data['name']
		location = form.cleaned_data['location']

		update_information = {
			'name': name,
			'location': location
		}

		headquarter_service.update(headquearter_id, update_information)

		return HttpResponseRedirect(reverse('TBD'))
	headquarter = headquarter_service.update(headquearter_id, update_information)

	return HttpResponseRedirect(reverse('TBD'))


	
