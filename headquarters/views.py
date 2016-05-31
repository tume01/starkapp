from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.HeadquarterService import HeadquarterService

from Adapters.FormValidator import FormValidator
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import HeadquarterForm

# Create your views here.

@require_http_methods(['GET'])
def index(request):
	headquarter_service = HeadquarterService()
	
	#filters = headquarters_filter(request)
	headquarters = headquarter_service.getHeadquarters()
	paginator = Paginator(headquarters, 10)

	page = request.GET.get('page')

	try:
		headquarters = paginator.page(page)
	except PageNotAnInteger:
		headquarters = paginator.page(1)
	except EmptyPage:
		headquarters = paginator.page(paginator.num_pages)

	context = {
		'titulo': 'Title',
		'headquarters': headquarters
	}

	return render(request, 'Admin/Headquarters/index_headquarter.html', context)

def headquarters_filter(request):
	filters = {}

	if request.GET.get('name'):
		filters['name'] = request.GET.get('name')

	if request.GET.get('description'):
		filters['description'] = request.GET.get('description')

	if request.GET.get('location'):
		filters['location'] = request.GET.get('location')

	return filters

@require_http_methods(['POST'])
def create_headquarters(request):
	request = FormValidator.validateForm(form, request)

	if not request:
		name = form.cleaned_data['name']
		location = form.cleaned_data['location']

		insert_data = {
			'name': name,
			'description': description,
			'location': location
		}

		headquarter_service.create(insert_data)

		return HttpResponseRedirect(reverse('headquarter:index'))
	else:
		return render(request, 'headquarter:index', context)

@require_http_methods(['POST'])	
def update(request, headquearter_id):
	headquearter_id = request.GET.get('headquarter_id')

	form = HeadquarterForm(request.POST)
	headquarter_service = HeadquarterService()

	if FormValidator.validateForm(form, request):
		context = {
			'titulo': 'titulo'
		}
		return render(request, 'headquarter:index', context)
	else:
		headquarter_service = HeadquarterService()

		name = form.cleaned_data['name']
		description = form.cleaned_data['description']
		location = form.cleaned_data['location']

		update_information = {
			'name': name,
			'description': description,
			'location': location
		}

		headquarter_service.update(headquearter_id, update_information)

		return HttpResponseRedirect(reverse('headquarter:index'))
	headquarter = headquarter_service.update(headquearter_id, update_information)

	return HttpResponseRedirect(reverse('headquarter:index'))
